from django.test import TestCase
from .models import Farmacia, Medicamento

class MedicamentoTests(TestCase):
    def test_create_medicamento(self):
        farmacia = Farmacia.objects.create(nome="Farmácia Teste", endereco="Rua Teste, 123")
        medicamento = Medicamento.objects.create(nome="Dipirona", nome_generico="Dipirona Sódica", preco=5.50, farmacia=farmacia)
        self.assertEqual(medicamento.nome, 'Dipirona')
        self.assertEqual(medicamento.farmacia.nome, 'Farmácia Teste')
