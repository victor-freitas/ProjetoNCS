from django.urls import path
from django.contrib.auth.views import login, logout
from application.users.views import cadastrar_usuario_view

urlpatterns = [
     path('Cadastro_usuario/', cadastrar_usuario_view),
     path('Login/', login, {'template_name':'login.html'}, name="login"),
     path('logout/', logout, {'next_page': 'login'}, name='sair'),
 ]
