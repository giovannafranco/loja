# coding: utf-8

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render

from produto.models import Produto


@login_required
def home(request):
    produtos = Produto.objects.all()
    print produtos
    return render(request, 'home/index.html', {'produtos': produtos})


@login_required
def adicionar_produto_carrinho(request, produto_id):
    if 'carrinho' not in request.session:
        request.session['carrinho'] = []

    carrinho = request.session['carrinho']

    carrinho.append(Produto.objects.get(pk=produto_id).id)

    messages.success(request, 'Produto adicionado no carrinho com sucesso!')

    return render(request, 'home/index.html')
