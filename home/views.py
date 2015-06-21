# coding: utf-8

from django.shortcuts import render


def home(request):
	return render(request, 'home/index.html', {'message': 'Olá mundo'})
