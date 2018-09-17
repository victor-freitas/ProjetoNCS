from django.shortcuts import render, redirect
from django.http import request
from application.core.form import FormProduto, FormCliente, FormFornecedor, FormMateriaPrima
from django.conf import settings

def index(request):
    return render(request, "index.html")

def Cliente(request):

    if request.POST:
        form = FormCliente(request.POST)
        if form.is_valid:
            form.save()
            return redirect(settings.INDEX_URL)
    else:
        form = FormCliente()
    return render(request, "cliente.html")

def Fornecedor(request):

    if request.POST:
        form = FormFornecedor(request.POST)
        if form.is_valid:
            form.save()
            return redirect(settings.INDEX_URL)
    else:
        form = FormFornecedor()
    return render(request, "fornecedor.html")

def MateriaPrimaView(request):

    if request.POST:
        form = FormMateriaPrima(request.POST)
        if form.is_valid:
            form.save()
            return redirect(settings.INDEX_URL)
    else:
        form = FormMateriaPrima()
    return render(request, "cad_materia_prima.html")

def cad_produto_views(request):

    if request.POST:
        form = FormProduto(request.POST)
        if form.is_valid:
            form.save()
            return redirect(settings.INDEX_URL)
    else:
        form = FormProduto()
    return render(request, "cad_produto.html")
# Create your views here.
