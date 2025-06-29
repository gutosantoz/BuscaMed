from django.contrib.auth.models import AbstractUser
from django.db import models

class Cliente(AbstractUser):
    telefone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(unique=True)
    nome = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.username
