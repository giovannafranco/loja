# coding: utf-8

from django.conf import settings
from django.db import models

#Classe carrinho que possui os atributos valor e compra
class Carrinho(models.Model):
    valor = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    compra = models.OneToOneField('Compra', related_name='carrinho', null=True)

    #Função equivalente ao toString(); retora o id do carrinho
    def __unicode__(self):
        return '<Carrinho: %s>' % self.id

#Classe ItemCarrinho que possui os atributos produto, carrinho, quantidade e valor
class ItemCarrinho(models.Model):
    produto = models.ForeignKey('produto.Produto')
    carrinho = models.ForeignKey('Carrinho', related_name='items')
    quantidade = models.IntegerField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    #Função equivalente ao toString(); retora o id do ItemCarrinho
    def __unicode__(self):
        return '<ItemCarrinho: %s>' % self.id

#Classe Compra que possui os atributos data e cliente
class Compra(models.Model):
    data = models.DateTimeField(auto_now=True)
    cliente = models.ForeignKey(settings.AUTH_USER_MODEL, null=True)

    #Função equivalente ao toString(); retora o id da compra
    def __unicode__(self):
        return '<Compra: %s>' % self.id
