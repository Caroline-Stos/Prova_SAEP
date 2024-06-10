from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser
from .users import CustomUserManager

class CustomUser(AbstractBaseUser):
        
    email = models.EmailField(unique=True, null=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager().create_user

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

class Professor(models.Model):
    nome = models.CharField(max_length=100)
    escola = models.CharField(max_length=100)
    user =  models.OneToOneField(
        settings.AUTH_USER_MODEL, 
        verbose_name='Usuário', 
        on_delete=models.CASCADE
    )

class Turma(models.Model):
    nome = models.CharField(max_length=100)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    data_criacao = models.DateTimeField('Data de Criação', auto_now_add=True)

class Atividade(models.Model):
    nome = models.CharField(max_length=100)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    data_criacao = models.DateTimeField('Data de Criação', auto_now_add=True)
