from django.urls import path
from . import views

urlpatterns = [
    path("", views.lista, name="lista"),
    # novas rotas nos passos 5, 6 e 7
    path("novo/", views.novo, name="novo"),
    path("novo/salvar/", views.salvar_novo,
        name="salvar_novo"),
    path("<int:id>/editar/", views.editar,
        name="editar"),
    path("<int:id>/editar/salvar/", views.salvar_edicao,
        name="salvar_edicao"),
    path("<int:id>/excluir/", views.excluir,
        name="excluir"),

]
