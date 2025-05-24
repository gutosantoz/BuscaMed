from django.shortcuts import render
from django.http import HttpResponse

def busca(request):
    return render(request, 'busca.html')