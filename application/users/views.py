from django.shortcuts import render, redirect
from application.users.forms import FormUsuario

def cadastrar_usuario_view(request):

    if request.POST:
        form = FormUsuario(request.POST)
        if form.is_valid:
            form.save()
    else:
        form = FormUsuario()
    return render(request, "users/cadastro_usuario.html")



# Create your views here.
