from django.urls import path
from . import views

urlpatterns = [
    path('ver_cliente/', views.ver_cliente, name="ver_cliente"),
    path('criar_cliente/', views.criar_cliente, name="criar_cliente"),
    path('login/', views.login, name="login")
  

]