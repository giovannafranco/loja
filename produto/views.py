# coding: utf-8

from django.shortcuts import render

from produto.models import Produto

#Função de retorna para a página detalhes de produto o detalhes de um determinado produto e os produtos relacionados, que são os produtos de mesma categoria
def detalhe_produto(request, produto_slug):
    produto = Produto.objects.get(slug=produto_slug)
    produtos_relacionados = Produto.objects.filter(
        categoria__descricao=produto.categoria.descricao).exclude(pk=produto.id) 
    return render(request, 'produto/detalhe_produto.html',
                  {
                      'produto': produto,
                      'produtos_relacionados': produtos_relacionados
                  })
