from django.contrib import admin

from produto.models import Produto, Categoria

admin.site.register(Produto)
admin.site.register(Categoria)
