from django.urls import path
from . import views

app_name = "alertas"

urlpatterns = [
    path("",                          views.painel,         name="painel"),
    path("disparar/",                 views.disparar,       name="disparar"),
    path("config/criar/",             views.config_criar,   name="config_criar"),
    path("config/<int:pk>/editar/",   views.config_editar,  name="config_editar"),
    path("config/<int:pk>/excluir/",  views.config_excluir, name="config_excluir"),
    path("alerta/<int:pk>/ignorar/",  views.ignorar_alerta, name="ignorar"),
    path("alerta/<int:pk>/reenviar/", views.reenviar_alerta,name="reenviar"),
]
