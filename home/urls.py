from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="principal"),
    path('sobre', views.sobre, name="sobre"),
    path('perfil/<str:usuario>/', views.perfil, name='perfil'),
    path('teste/<int:codigo>/<str:nome>/', views.teste, name='teste'),

    path('produto', views.produto, name='produto'),
    path('form_produto', views.form_produto, name='form_produto'),
    path('editar/<int:pk>/', views.editar_produto, name='editar_produto'),
    path('remover/<int:pk>/', views.remover_produto, name='remover_produto'),
    path('detalhes/<int:pk>/', views.detalhes_produto, name='detalhes_produto'),
    path('listagem', views.listagem_produto, name='listagem_produto'),
    path('qtde_produto/', views.qtde_produto, name='qtde_produto'),
    path('relatorio/', views.relatorio_produto, name='relatorio_produto'),

]

