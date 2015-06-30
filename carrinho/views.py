# coding: utf-8

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect

from produto.models import Produto
from carrinho.models import Carrinho, Compra, ItemCarrinho

#função que adicionar um produt ao carrinho 
def adicionar_produto_carrinho(request, produto_slug, quantidade):
    produto = Produto.objects.get(slug=produto_slug) #produto recebe um produto com a slug que é passada // slug = bolsa-amarelo

    if 'carrinho' not in request.session: # se o carrinho não está na sessão
        carrinho = Carrinho() #carrinho recebe um novo carrinho
        carrinho.save() 
        request.session['carrinho'] = carrinho # a sessão recebe o novo carrinho que foi criado

    if not _verificar_estoque_disponivel(request, produto_slug, quantidade):#chama a função para verificar estoque, passando o produto e quantidade
        messages.error(request, 'Quantidade indisponível!')
        return redirect('detalhe_produto', produto_slug=produto_slug) # redireciona para a página de detalhes do produto

    carrinho = request.session.get('carrinho') # carrinho recebe o carrinho da sessão

    item_no_carrinho = _procurar_item_no_carrinho(carrinho, produto_slug) #variável recebe um boolean que informa se já existe um item desse no carrinho

    if not item_no_carrinho: # se produto não existe
        item_carrinho = ItemCarrinho() # item_carrinho recebe novo ItemCarrinho
        item_carrinho.produto = produto
        item_carrinho.carrinho = carrinho
        item_carrinho.quantidade = int(quantidade)
        item_carrinho.valor = produto.valor * item_carrinho.quantidade # valor é atualizado conforme a quantidade de produto
        item_carrinho.save()
        request.session['carrinho'] = carrinho
        messages.success(request, 'Produto adicionado no carrinho com sucesso!')
    else: # se produto existe
        item = item_no_carrinho # item recebe o item_no_carrinho 
        item.quantidade += int(quantidade) # quantidade recebe ela mesma mas a quantidade infrmada
        item.valor = item.produto.valor * item.quantidade # valor é atualizado conforme a quantidade de produto
        item.save()
        messages.info(request, 'Produto atualizado com sucesso!')

    _calcula_valor_carrinho(request) # o valor do carrinho é recalculado

    request.session['carrinho'] = carrinho

    return redirect('mostrar_carrinho') #redireciona para a página mostrar_carrinho

#função que mostra o carrinho de compra com os produtos comprados
def mostrar_carrinho(request):
    carrinho = request.session.get('carrinho', Carrinho())
    #retorna a página carrinho.html com a lista de produtos e o otal de compra
    return render(request, 'home/carrinho.html',
                  {
                      'produtos': carrinho.items.all(),
                      'total': carrinho.valor or 0
                  }
                  )

#Função que atualiza a quantidade de itens no carrinho  
def atualizar_quantidade_item_carrinho(request, id_item, quantidade):
    item = ItemCarrinho.objects.get(pk=id_item) # pega o item pelo id

    #verifica quantidade disponível no estoque
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

#Função que remove produto do carrinho
def remover_produto_carrinho(request, id_item):
    item = ItemCarrinho.objects.get(pk=id_item)
    item.delete()

    _calcula_valor_carrinho(request)

    return redirect('mostrar_carrinho')


#Função que  finaliza a compra // o @login_required informa que essa função exige que o usuário faço login primeiro
@login_required
def fechar_compra(request):
    carrinho = request.session.get('carrinho', Carrinho())

    compra = Compra() 
    compra.cliente = request.user #cliente recebe o usuário que está logado
    compra.save()

    carrinho.compra = compra
    carrinho.save()

    _dar_baixa_estoque(carrinho) # é dado baixo que todos os produto que foram comprados

    messages.success(request, 'Compra finalizada com sucesso!')

    del request.session['carrinho'] #carrinho agora é excluido e é guardado a compra correspondente ao carrinho

    return redirect('home') # é redirecionado para a página home

#necessita de login
#Função que mostrar o histórico de compras do usuário que está logado
@login_required
def minhas_compras(request):
    usuario = request.user 
    compras = Compra.objects.filter(cliente_id=usuario.id) # compras irá recebe somente compras feitas pelo usuário logado // filter, filtra o usuário que realizou a compra
    return render(request, 'carrinho/minhas_compras.html', {'compras': compras}) 

#Função que calcula o valor total do carrinho
def _calcula_valor_carrinho(request):
    carrinho = request.session.get('carrinho', Carrinho())

    valor = sum([item.valor for item in carrinho.items.all()]) # é feito a soma dos valores de cada produto

    carrinho.valor = valor
    carrinho.save()

    request.session['carrinho'] = carrinho


#Função que verificar se há produto no estoque
def _verificar_estoque_disponivel(request, produto_slug, quantidade, considerar_sessao=True):
    carrinho = request.session.get('carrinho', Carrinho())

    item_no_carrinho = _procurar_item_no_carrinho(carrinho, produto_slug) # devolve um boolean informando se há ou não produto no carrinho

    if item_no_carrinho and considerar_sessao: # se ainda tiver produt no estoque
        quantidade = int(quantidade) + item_no_carrinho.quantidade # somar quantidade com quantidade no carrinho

    produto = Produto.objects.get(slug=produto_slug)

    return produto.qtd_estoque >= int(quantidade)

#Função que procura se já existe produto no carrinho 
def _procurar_item_no_carrinho(carrinho, produto_slug):
    lista = filter(lambda x: x.produto.slug == produto_slug, carrinho.items.all())#verifica se o produto passado por parametro está no carrinho de compras, ele compara a slug
    produto = None
    if lista:
        produto = lista[0]
    return produto

#Função que mostra detalhes da compra
def detalhe_compra(request, id_compra): 
    compra = Compra.objects.get(pk=id_compra) # compra recebe a compra que tem o id passado
    return render(request, 'carrinho/items_compra.html',# redireciona para paǵina itens_compra passando os itens daquela compra
                  {
                      'items': compra.carrinho.items.all()
                  })

#Função que dá baixa no estoque
def _dar_baixa_estoque(carrinho):
    for item in carrinho.items.all():
        produto = item.produto
        produto.qtd_estoque -= item.quantidade
        produto.save()
