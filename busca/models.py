from django.db import models

class Farmacia(models.Model):
    nome = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255)
    telefone = models.CharField(max_length=20, blank=True)
    horario_funcionamento = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.nome


class Medicamento(models.Model):
    nome = models.CharField(max_length=255)
    nome_generico = models.CharField(max_length=255)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    farmacia = models.ForeignKey(Farmacia, related_name='medicamentos', on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
