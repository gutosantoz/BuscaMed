from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Cliente

class ClienteCreationForm(UserCreationForm):
    class Meta:
        model = Cliente
        fields = ('username', 'email', 'telefone', 'endereco', 'password1', 'password2')
