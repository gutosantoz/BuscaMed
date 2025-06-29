from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Cliente
from .forms import ClienteCreationForm

class ClienteAdmin(UserAdmin):
    add_form = ClienteCreationForm
    model = Cliente
    list_display = ['username', 'email', 'telefone', 'endereco', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('telefone', 'endereco')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('telefone', 'endereco')}),
    )

admin.site.register(Cliente, ClienteAdmin)
