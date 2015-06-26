from django.db import models


class Produto(models.Model):
	descricao = models.CharField(max_length=45)
	imagem = models.FileField()
	qtdEstoque = models.IntegerField()
	valor = models.DecimalField(max_digits=10, decimal_places=2)

	def __str__(self):
		return self.descricao
