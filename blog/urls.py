from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('<slug:slug>/', views.artigo_detalhe, name='artigo_detalhe'),
] 