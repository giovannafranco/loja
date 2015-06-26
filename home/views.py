# coding: utf-8

from django.shortcuts import render

from produto.models import Produto


def home(request):
	produtos = Produto.objects.all()
	return render(request, 'home/index.html', {'produtos': produtos})

def adicionar_produto_carrinho(request, produto_id):
	if 'carrinho' not in request.session:
		request.session['carrinho'] = []

	carrinho = request.session['carrinho']

	carrinho.append(Produto.objects.get(pk=produto_id).id)

	return render(request, 'home/index.html', {'produtos': None, 'mensagem': 'show parça'})
