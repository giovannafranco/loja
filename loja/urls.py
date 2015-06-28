from django.conf.urls import include, url
from django.contrib import admin

from home.views import home
from carrinho.views import adicionar_produto_carrinho, \
    mostrar_carrinho, atualizar_quantidade_item_carrinho


urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^produtos/(?P<produto_slug>[\w_-]+)/$', adicionar_produto_carrinho, name='adicionar_produto_carrinho'),

    url(r'^carrinho/$', mostrar_carrinho, name='mostrar_carrinho'),
    url(
        r'^carrinho/atualizar/(?P<id_item>[\d]+)/(?P<quantidade>[\d]+)/$',
        atualizar_quantidade_item_carrinho, name='atualizar_carrinho'
        ),
]
