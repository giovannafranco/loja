# coding: utf-8

from django.shortcuts import render

from produto.models import Produto, Categoria


def home(request):
    produtos = Produto.objects.all()
    categorias = Categoria.objects.all()
    return render(request, 'home/index.html',
                  {
                      'produtos': produtos,
                      'categorias': categorias
                  })


def listar_produtos(request, categoria):
    categorias = Categoria.objects.all()
    if categoria == 'todos':
        produtos = Produto.objects.all()
    else:
        produtos = Produto.objects.filter(categoria__slug=categoria)

    return render(request, 'home/index.html',
                  {
                      'produtos': produtos,
                      'categorias': categorias,
                      'categoria_selecionada': categoria
                  })
