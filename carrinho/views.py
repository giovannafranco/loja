# coding: utf-8

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render

from produto.models import Produto
from carrinho.models import Carrinho, ItemCarrinho


# @login_required
def adicionar_produto_carrinho(request, produto_slug):
    produto = Produto.objects.get(slug=produto_slug)

    if 'carrinho' not in request.session:
        carrinho = Carrinho()
        request.session['carrinho'] = carrinho
        carrinho.save()

    carrinho = request.session.get('carrinho')

    # verficando se o produto já foi adicionado no carrinho
    if not filter(lambda x: x.produto.slug == produto_slug, carrinho.items.all()):
        item_carrinho = ItemCarrinho()
        item_carrinho.produto = produto
        item_carrinho.carrinho = carrinho
        item_carrinho.quantidade = 1
        item_carrinho.valor = produto.valor
        item_carrinho.save()

        request.session['carrinho'] = carrinho
        messages.success(request, 'Produto adicionado no carrinho com sucesso!')

    carrinho.valor = _calcula_valor_carrinho(carrinho)
    carrinho.save()

    request.session['carrinho'] = carrinho

    return render(request, 'home/index.html')


# @login_required
def mostrar_carrinho(request):
    carrinho = request.session.get('carrinho', [])
    return render(request, 'home/carrinho.html',
                  {
                      'produtos': carrinho.items.all(),
                      'total': carrinho.valor
                  }
                  )


def atualizar_quantidade_item_carrinho(request, id_item, quantidade):
    item = ItemCarrinho.objects.get(pk=id_item)
    item.quantidade = quantidade
    item.valor = item.produto.valor * int(quantidade)
    item.save()

    carrinho = item.carrinho
    carrinho.valor = _calcula_valor_carrinho(carrinho)
    carrinho.save()

    return JsonResponse({'total': carrinho.valor, 'item_valor': item.valor})


def _calcula_valor_carrinho(carrinho):
    return sum([item.valor for item in carrinho.items.all()])
