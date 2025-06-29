from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Cliente

class ClienteAdmin(UserAdmin):
    model = Cliente
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('telefone', 'endereco')}),
    )

admin.site.register(Cliente, ClienteAdmin)
