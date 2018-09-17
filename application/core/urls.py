from django.urls import path
from application.core.views import Fornecedor, Cliente, MateriaPrimaView, index, cad_produto_views

urlpatterns = [
    path('Fornecedor/', Fornecedor, name='cadastro_fornecedor' ),
    path('Cliente/', Cliente, name='cadastro_cliente' ),
    path('MateriaPrima/', MateriaPrimaView, name='cadastro_materia' ),
    path('index/', index, name='index' ),
    path('', index),
    path('cad_produto/', cad_produto_views, name='cad_produto'),
]
