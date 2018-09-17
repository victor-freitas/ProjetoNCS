from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UsuarioManager(BaseUserManager):

    def _criar_usuario(self, login, password, **Campos_extra):
        if not login:
            raise ValueError("username deve ser declarado!")
        user = self.model(login=login, **Campos_extra)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, login, password, **Campos_extra):
        return sef._criar_usuario(self, login, password, **Campos_extra)

    def create_superuser(self, login, password, **Campos_extra):
        return self._criar_usuario(login, password, **Campos_extra)

class Usuario(AbstractBaseUser, PermissionsMixin):
    login = models.CharField('login', max_length=250, unique=True)
    name = models.CharField('Nome', max_length=400)
    email = models.EmailField('E-mail', max_length=200, unique=True)
    is_active = models.BooleanField('Está ativo?', blank=True, default=True)
    is_staff = models.BooleanField('É da equipe?', blank=True, default=True)
    date_joined = models.DateTimeField('Data de entrada', auto_now_add=True)

    objects = UsuarioManager()

    USERNAME_FIELD = 'login'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.login or self.name

    def get_short_name(self):
        return self.login

    def get_full_name(self):
        return str(self)

    def has_module_perms(self, package_name):
        return True

    def has_perm(self, perm, obj=None):
        return True

    def has_perms(self, perm_list, obj=None):
        return True


    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'


# Create your models here.
