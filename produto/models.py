# coding: utf-8

from django.db import models

#Classe Produto que tem os atributos descricao, imagem, qtd_estoque, valor, categoria e slug
class Produto(models.Model):
    descricao = models.CharField(max_length=45)
    imagem = models.ImageField(upload_to='fotos_produto/')
    qtd_estoque = models.IntegerField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey('Categoria')
    slug = models.SlugField()

    def __unicode__(self):
        return self.descricao

#Classe Categoria que tem os atributos descricao e slug
class Categoria(models.Model):
    descricao = models.CharField(max_length=20)
    slug = models.SlugField()

    def __unicode__(self):
        return self.descricao
