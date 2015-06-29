# coding: utf-8

from django.conf import settings
from django.db import models


class Carrinho(models.Model):
    valor = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    compra = models.OneToOneField('Compra', related_name='carrinho', null=True)

    def __unicode__(self):
        return '<Carrinho: %s>' % self.id


class ItemCarrinho(models.Model):
    produto = models.ForeignKey('produto.Produto')
    carrinho = models.ForeignKey('Carrinho', related_name='items')
    quantidade = models.IntegerField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __unicode__(self):
        return '<ItemCarrinho: %s>' % self.id


class Compra(models.Model):
    data = models.DateTimeField(auto_now=True)
    cliente = models.ForeignKey(settings.AUTH_USER_MODEL, null=True)

    def __unicode__(self):
        return '<Compra: %s>' % self.id
