from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import QuemSomos, Contato
from projects.models import Projeto
from blog.models import Artigo
from representatives.models import Representante

def home(request):
    """Página inicial da landing page"""
    projetos_destaque = Projeto.objects.filter(destaque=True)[:3]
    artigos_recentes = Artigo.objects.filter(publicado=True)[:3]
    quem_somos = QuemSomos.objects.first()
    
    context = {
        'projetos_destaque': projetos_destaque,
        'artigos_recentes': artigos_recentes,
        'quem_somos': quem_somos,
    }
    return render(request, 'app/home.html', context)

def quem_somos(request):
    """Página quem somos"""
    quem_somos = QuemSomos.objects.first()
    representantes = Representante.objects.filter(ativo=True)
    
    context = {
        'quem_somos': quem_somos,
        'representantes': representantes,
    }
    return render(request, 'app/quem_somos.html', context)

def contato(request):
    """Página de contato com formulário funcional"""
    if request.method == 'POST':
        nome_completo = request.POST.get('nome_completo')
        telefone = request.POST.get('telefone')
        email = request.POST.get('email')
        assunto = request.POST.get('assunto')
        mensagem = request.POST.get('mensagem')
        
        # Criar objeto de contato
        contato = Contato.objects.create(
            nome_completo=nome_completo,
            telefone=telefone,
            email=email,
            assunto=assunto,
            mensagem=mensagem
        )
        
        # Enviar email
        try:
            send_mail(
                f'Novo contato: {assunto}',
                f'''
                Nome: {nome_completo}
                Telefone: {telefone}
                Email: {email}
                Assunto: {assunto}
                Mensagem: {mensagem}
                ''',
                settings.EMAIL_HOST_USER,
                [settings.EMAIL_HOST_USER],
                fail_silently=False,
            )
            messages.success(request, 'Mensagem enviada com sucesso! Entraremos em contato em breve.')
        except Exception as e:
            messages.error(request, 'Erro ao enviar email. Tente novamente.')
        
        return redirect('contato')
    
    return render(request, 'app/contato.html')
