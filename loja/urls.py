from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from home.views import home, listar_produtos
from carrinho.views import adicionar_produto_carrinho, \
    mostrar_carrinho, atualizar_quantidade_item_carrinho, \
    remover_produto_carrinho, fechar_compra, minhas_compras, detalhe_compra
from produto.views import detalhe_produto


urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout'),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^produto/(?P<produto_slug>[\w_-]+)/$',
        detalhe_produto,
        name='detalhe_produto'),
    url(r'^produtos/(?P<categoria>[\w_-]+)', listar_produtos, name='listar_produtos'),

    url(
        r'^carrinho/adicionar/(?P<produto_slug>[\w_-]+)/(?P<quantidade>[\d]+)/$',
        adicionar_produto_carrinho,
        name='adicionar_produto_carrinho'
        ),
    url(r'^carrinho/$', mostrar_carrinho, name='mostrar_carrinho'),
    url(
        r'^carrinho/atualizar/(?P<id_item>[\d]+)/(?P<quantidade>[\d]+)/$',
        atualizar_quantidade_item_carrinho, name='atualizar_carrinho'
        ),
    url(r'^carrinho/excluir/(?P<id_item>[\d]+)/$', remover_produto_carrinho, name='remover_produto_carrinho'),

    url(r'^compras/$', minhas_compras, name='minhas_compras'),
    url(r'^compra/(?P<id_compra>[\d]+)/$', detalhe_compra, name='detalhe_compra'),
    url(r'^compra/fechar/$', fechar_compra, name='fechar_compra'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
