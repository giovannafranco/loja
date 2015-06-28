# coding: utf-8

from django.shortcuts import render

from produto.models import Produto


def home(request):
    produtos = Produto.objects.all()
    return render(request, 'home/index.html', {'produtos': produtos})
