from django import forms
from application.users.models import Usuario

class FormUsuario(forms.ModelForm):
    class Meta:
        model = Usuario
        fields =    ['login', 'name', 'email']
