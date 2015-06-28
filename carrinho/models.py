# coding: utf-8

from django.db import models


class Carrinho(models.Model):
    valor = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    # compra = models.ForeignKey('compra.Compra')

    def __unicode__(self):
        return '<Carrinho: %s>' % self.id


class ItemCarrinho(models.Model):
    produto = models.ForeignKey('produto.Produto')
    carrinho = models.ForeignKey('Carrinho', related_name='items')
    quantidade = models.IntegerField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __unicode__(self):
        return '<ItemCarrinho: %s>' % self.id
