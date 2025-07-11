from django.urls import path
from . import views

urlpatterns = [
    path('', views.projetos, name='projetos'),
    path('<int:projeto_id>/', views.projeto_detalhe, name='projeto_detalhe'),
] 