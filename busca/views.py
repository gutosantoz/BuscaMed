from django.shortcuts import render
from .models import Medicamento, Farmacia

def busca(request):
    query = request.GET.get('q')  # Recebe o termo de pesquisa via GET
    if query:
        # Realiza a busca no banco de dados
        medicamentos = Medicamento.objects.filter(nome__icontains=query)
    else:
        medicamentos = Medicamento.objects.none()

    resultados = []
    for medicamento in medicamentos:
        farmacia_info = {
            'nome_farmacia': medicamento.farmacia.nome,
            'preco': medicamento.preco,
            'endereco': medicamento.farmacia.endereco,
            'telefone': medicamento.farmacia.telefone,
        }
        resultados.append(farmacia_info)

    return render(request, 'busca.html', {'resultados': resultados})
