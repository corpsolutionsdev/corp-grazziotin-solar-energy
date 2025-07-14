from django.db import models

# Create your models here.

class Artigo(models.Model):
    titulo = models.CharField(max_length=200, verbose_name="Título")
    slug = models.SlugField(
        max_length=200, 
        unique=True, 
        blank=True,
        verbose_name="Slug",
        help_text="Versão amigável da URL do artigo. Ex: 'como-instalar-paineis-solares' para o título 'Como Instalar Painéis Solares'. Deixe em branco para gerar automaticamente."
    )
    imagem = models.ImageField(upload_to='blog/', verbose_name="Imagem do Artigo")
    descricao = models.TextField(max_length=500, verbose_name="Descrição")
    data_publicacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    publicado = models.BooleanField(default=True, verbose_name="Publicado")

    class Meta:
        verbose_name = "Artigo"
        verbose_name_plural = "Artigos"
        ordering = ['-data_publicacao']

    def __str__(self):
        return self.titulo

    def save(self, *args, **kwargs):
        if not self.slug:
            from django.utils.text import slugify
            self.slug = slugify(self.titulo)
        super().save(*args, **kwargs)
