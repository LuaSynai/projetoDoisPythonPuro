from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('escrever/', views.escrever, name='escrever'),
    path('cadastrar_pessoas/', views.cadastrar_pessoas, name='cadastrar_pessoas'),
    path('dia/', views.dia, name='dia'),
    path('excluir_dia/', views.excluir_dia, name='excluir_dia')   

]