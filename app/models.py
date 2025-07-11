from django.db import models

# Create your models here.

class QuemSomos(models.Model):
    titulo = models.CharField(max_length=200, verbose_name="Título")
    descricao = models.TextField(verbose_name="Descrição")
    imagem = models.ImageField(upload_to='quem_somos/', verbose_name="Imagem da Empresa")
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Quem Somos"
        verbose_name_plural = "Quem Somos"

    def __str__(self):
        return self.titulo

class Contato(models.Model):
    ASSUNTO_CHOICES = [
        ('orcamento', 'Orçamento'),
        ('suporte', 'Suporte Técnico'),
        ('informacao', 'Informação'),
    ]
    
    nome_completo = models.CharField(max_length=200, verbose_name="Nome Completo")
    telefone = models.CharField(max_length=20, verbose_name="Telefone")
    email = models.EmailField(verbose_name="E-mail")
    assunto = models.CharField(max_length=20, choices=ASSUNTO_CHOICES, verbose_name="Assunto")
    mensagem = models.TextField(verbose_name="Mensagem")
    data_envio = models.DateTimeField(auto_now_add=True)
    lido = models.BooleanField(default=False, verbose_name="Mensagem Lida")

    class Meta:
        verbose_name = "Contato"
        verbose_name_plural = "Contatos"
        ordering = ['-data_envio']

    def __str__(self):
        return f"{self.nome_completo} - {self.assunto}"
