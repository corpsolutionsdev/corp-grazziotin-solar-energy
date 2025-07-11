from django.db import models

# Create your models here.

class Projeto(models.Model):
    titulo = models.CharField(max_length=200, verbose_name="Título")
    descricao = models.TextField(verbose_name="Descrição")
    imagem = models.ImageField(upload_to='projetos/', verbose_name="Imagem do Projeto")
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    destaque = models.BooleanField(
        default=False, 
        verbose_name="Projeto em Destaque",
        help_text="Marque esta opção para exibir o projeto na seção de destaque da página inicial. Apenas os projetos marcados aparecerão no carrossel da home."
    )

    class Meta:
        verbose_name = "Projeto"
        verbose_name_plural = "Projetos"
        ordering = ['-data_criacao']

    def __str__(self):
        return self.titulo
