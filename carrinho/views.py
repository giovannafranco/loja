# coding: utf-8

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect

from produto.models import Produto
from carrinho.models import Carrinho, Compra, ItemCarrinho


def adicionar_produto_carrinho(request, produto_slug, quantidade):
    produto = Produto.objects.get(slug=produto_slug)

    if 'carrinho' not in request.session:
        carrinho = Carrinho()
        carrinho.save()
        request.session['carrinho'] = carrinho

    if not _verificar_estoque_disponivel(request, produto_slug, quantidade):
        messages.error(request, 'Quantidade indisponível!')
        return redirect('detalhe_produto', produto_slug=produto_slug)

    carrinho = request.session.get('carrinho')

    item_no_carrinho = _procurar_item_no_carrinho(carrinho, produto_slug)

    if not item_no_carrinho:
        item_carrinho = ItemCarrinho()
        item_carrinho.produto = produto
        item_carrinho.carrinho = carrinho
        item_carrinho.quantidade = int(quantidade)
        item_carrinho.valor = produto.valor * item_carrinho.quantidade
        item_carrinho.save()
        request.session['carrinho'] = carrinho
        messages.success(request, 'Produto adicionado no carrinho com sucesso!')
    else:
        item = item_no_carrinho
        item.quantidade += int(quantidade)
        item.valor = item.produto.valor * item.quantidade
        item.save()
        messages.info(request, 'Produto atualizado com sucesso!')

    _calcula_valor_carrinho(request)

    request.session['carrinho'] = carrinho

    return redirect('mostrar_carrinho')


def mostrar_carrinho(request):
    carrinho = request.session.get('carrinho', Carrinho())
    return render(request, 'home/carrinho.html',
                  {
                      'produtos': carrinho.items.all(),
                      'total': carrinho.valor or 0
                  }
                  )


def atualizar_quantidade_item_carrinho(request, id_item, quantidade):
    item = ItemCarrinho.objects.get(pk=id_item)

    if not _verificar_estoque_disponivel(request, item.produto.slug, quantidade, False):
        messages.error(request, 'Quantidade indisponível!')
        request.status_code = 500
        return request

    item = ItemCarrinho.objects.get(pk=id_item)
    item.quantidade = quantidade
    item.valor = item.produto.valor * int(quantidade)
    item.save()

    _calcula_valor_carrinho(request)

    return JsonResponse({'total': item.carrinho.valor, 'item_valor': item.valor})


def remover_produto_carrinho(request, id_item):
    item = ItemCarrinho.objects.get(pk=id_item)
    item.delete()

    _calcula_valor_carrinho(request)

    return redirect('mostrar_carrinho')


@login_required
def fechar_compra(request):
    carrinho = request.session.get('carrinho', Carrinho())

    compra = Compra()
    compra.cliente = request.user
    compra.save()

    carrinho.compra = compra
    carrinho.save()

    _dar_baixa_estoque(carrinho)

    messages.success(request, 'Compra finalizada com sucesso!')

    del request.session['carrinho']

    return redirect('home')


@login_required
def minhas_compras(request):
    usuario = request.user
    compras = Compra.objects.filter(cliente_id=usuario.id)
    return render(request, 'carrinho/minhas_compras.html', {'compras': compras})


def _calcula_valor_carrinho(request):
    carrinho = request.session.get('carrinho', Carrinho())

    valor = sum([item.valor for item in carrinho.items.all()])

    carrinho.valor = valor
    carrinho.save()

    request.session['carrinho'] = carrinho


def _verificar_estoque_disponivel(request, produto_slug, quantidade, considerar_sessao=True):
    carrinho = request.session.get('carrinho', Carrinho())

    item_no_carrinho = _procurar_item_no_carrinho(carrinho, produto_slug)

    if item_no_carrinho and considerar_sessao:
        quantidade = int(quantidade) + item_no_carrinho.quantidade

    produto = Produto.objects.get(slug=produto_slug)

    return produto.qtd_estoque >= int(quantidade)


def _procurar_item_no_carrinho(carrinho, produto_slug):
    lista = filter(lambda x: x.produto.slug == produto_slug, carrinho.items.all())
    produto = None
    if lista:
        produto = lista[0]
    return produto


def detalhe_compra(request, id_compra):
    compra = Compra.objects.get(pk=id_compra)
    return render(request, 'carrinho/items_compra.html',
                  {
                      'items': compra.carrinho.items.all()
                  })


def _dar_baixa_estoque(carrinho):
    for item in carrinho.items.all():
        produto = item.produto
        produto.qtd_estoque -= item.quantidade
        produto.save()
