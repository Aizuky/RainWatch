from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    nome_completo = models.CharField(max_length=150, verbose_name="Nome completo", blank=True, null=True)
    email = models.EmailField(unique=True, verbose_name="Email")

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email", "nome_completo"]

    def __str__(self):
        return f"{self.nome_completo} ({self.username})"
