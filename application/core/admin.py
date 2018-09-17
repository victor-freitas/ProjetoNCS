from django.contrib import admin
from application.core.models import Tipoproduto, Cliente, Fornecedor, Tiposeguimento, Materiaprima, Produto


# Register your models here.

admin.site.register(Cliente)
admin.site.register(Materiaprima)
admin.site.register(Fornecedor)
admin.site.register(Tiposeguimento)
admin.site.register(Tipoproduto)
admin.site.register(Produto)
