from django.urls import path
from . import views

urlpatterns = [
    path('busca/', views.busca, name='busca'),
]
