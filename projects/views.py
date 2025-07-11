from django.shortcuts import render
from .models import Projeto

# Create your views here.

def projetos(request):
    """Lista todos os projetos"""
    projetos = Projeto.objects.all()
    context = {
        'projetos': projetos,
    }
    return render(request, 'projects/projetos.html', context)

def projeto_detalhe(request, projeto_id):
    """Detalhes de um projeto específico"""
    try:
        projeto = Projeto.objects.get(id=projeto_id)
        context = {
            'projeto': projeto,
        }
        return render(request, 'projects/projeto_detalhe.html', context)
    except Projeto.DoesNotExist:
        return render(request, '404.html', status=404)
