from django.db import models

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(max_length=255)
    cel  = models.CharField(max_length=255)
    email = models.EmailField()
    endereco  = models.CharField(max_length=255)

    def __str__(self):
        return self.nome