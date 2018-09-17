from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from application.users.models import Usuario
from django import forms

class UsuarioForm(forms.ModelForm):

    def save(self, commit=True):
        usuario = super(UsuarioForm, self).save(commit=False)
        usuario.set_password("123@mudar")
        if commit:
            usuario.save()
        return usuario

    class Meta:
        model = Usuario
        fields = ["login", "name", "email"]

class UsuarioAlteraForm(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = ["login" ,"name", "email"]

class UsuarioAdmin(UserAdmin):

    add_form = UsuarioForm
    form = UsuarioAlteraForm
    add_fieldsets = ((None, {"fields": ("login", "name", "email")}),)
    fieldsets = ((None, {"fields": ("name", "email")}),)
    list_display = ["login", "name", "email"]
    filter_horizontal = []
    ordering = ["login"]
    list_filter = ["login"]

# Register your models here.
admin.site.register(Usuario, UsuarioAdmin)
