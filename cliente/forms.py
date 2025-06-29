from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Cliente

class ClienteCreationForm(UserCreationForm):
    class Meta:
        model = Cliente
        fields = (
            'username',     # nome de usuário para login
            'email',        # e-mail (já presente em AbstractUser)
            'telefone',     # campo personalizado
            'endereco',     # campo personalizado
            'password1',
            'password2',
        )
