from django.shortcuts import render, get_object_or_404
from .models import Artigo

# Create your views here.

def blog(request):
    """Lista todos os artigos do blog"""
    artigos = Artigo.objects.filter(publicado=True)
    context = {
        'artigos': artigos,
    }
    return render(request, 'blog/blog.html', context)

def artigo_detalhe(request, slug):
    """Detalhes de um artigo específico"""
    artigo = get_object_or_404(Artigo, slug=slug, publicado=True)
    context = {
        'artigo': artigo,
    }
    return render(request, 'blog/artigo_detalhe.html', context)
