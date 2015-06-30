# coding: utf-8

from django.shortcuts import render

from produto.models import Produto, Categoria

#Função que retorna para a página home os produtos qas categorias
def home(request):
    produtos = Produto.objects.all()
    categorias = Categoria.objects.all()
    return render(request, 'home/index.html',
                  {
                      'produtos': produtos,
                      'categorias': categorias
                  })

#Função que lista produtos pela categoria
def listar_produtos(request, categoria):
    categorias = Categoria.objects.all()
    if categoria == 'todos': # se a categoria for "todos"
        produtos = Produto.objects.all() # são selecionados todos os produtos
    else:
        produtos = Produto.objects.filter(categoria__slug=categoria) # senão é retornado os produtos que pertencem a categoria escolhida

    return render(request, 'home/index.html',
                  {
                      'produtos': produtos,
                      'categorias': categorias,
                      'categoria_selecionada': categoria
                  })
