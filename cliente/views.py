from django.shortcuts import render
from django.http import HttpResponse

def ver_cliente(request):
    return HttpResponse('Ola Cliente, tudo bem??')

def criar_cliente(request):
    return render(request, 'criar_cliente.html')

def login(request):
    return render(request, 'login.html')