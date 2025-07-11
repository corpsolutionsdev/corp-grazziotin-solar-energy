from django.db import models

# Create your models here.

class Representante(models.Model):
    nome = models.CharField(max_length=200, verbose_name="Nome")
    foto = models.ImageField(upload_to='representantes/', verbose_name="Foto")
    endereco = models.TextField(verbose_name="Endereço")
    telefone = models.CharField(max_length=20, verbose_name="Telefone")
    email = models.EmailField(verbose_name="E-mail", blank=True, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    ativo = models.BooleanField(default=True, verbose_name="Ativo")

    class Meta:
        verbose_name = "Representante"
        verbose_name_plural = "Representantes"
        ordering = ['nome']

    def __str__(self):
        return self.nome
