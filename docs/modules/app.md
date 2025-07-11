# App Principal

O módulo `app` é responsável pelas páginas institucionais da empresa Grazziotin Energia Solar.

## Visão Geral

Este módulo contém as funcionalidades principais do site institucional:

- Página inicial
- Seção "Quem Somos"
- Formulário de contato
- Navegação principal

## Modelos

### QuemSomos

Modelo para gerenciar informações sobre a empresa.

```python
class QuemSomos(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.titulo
```

### Contato

Modelo para armazenar mensagens recebidas via formulário.

```python
class Contato(models.Model):
    nome_completo = models.CharField(max_length=100)
    email = models.EmailField()
    assunto = models.CharField(max_length=200)
    mensagem = models.TextField()
    data_envio = models.DateTimeField(auto_now_add=True)
    lido = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.nome_completo} - {self.assunto}"
```

## Views

### home

View para a página inicial do site.

```python
def home(request):
    return render(request, 'app/home.html')
```

### quem_somos

View para a página institucional.

```python
def quem_somos(request):
    try:
        quem_somos = QuemSomos.objects.latest('data_atualizacao')
    except QuemSomos.DoesNotExist:
        quem_somos = None
    
    return render(request, 'app/quem_somos.html', {
        'quem_somos': quem_somos
    })
```

### contato

View para o formulário de contato.

```python
def contato(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Mensagem enviada com sucesso!')
            return redirect('contato')
    else:
        form = ContatoForm()
    
    return render(request, 'app/contato.html', {
        'form': form
    })
```

## URLs

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('quem-somos/', views.quem_somos, name='quem_somos'),
    path('contato/', views.contato, name='contato'),
]
```

## Templates

### home.html

Template da página inicial com design responsivo e moderno.

### quem_somos.html

Template da página institucional com informações sobre a empresa.

### contato.html

Template do formulário de contato com validação e feedback.

## Admin

Configuração personalizada do painel administrativo:

```python
@admin.register(QuemSomos)
class QuemSomosAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'data_criacao', 'data_atualizacao']
    search_fields = ['titulo', 'descricao']
    readonly_fields = ['data_criacao', 'data_atualizacao']

@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    list_display = ['nome_completo', 'email', 'assunto', 'data_envio', 'lido']
    list_filter = ['assunto', 'lido', 'data_envio']
    search_fields = ['nome_completo', 'email', 'mensagem']
    readonly_fields = ['data_envio']
    list_editable = ['lido']
```

## Funcionalidades

### Formulário de Contato

- Validação de campos obrigatórios
- Envio de email de confirmação
- Armazenamento no banco de dados
- Marcação de mensagens lidas/não lidas

### Gestão de Conteúdo

- Interface administrativa para editar informações
- Controle de versões com timestamps
- Preview de alterações
- Backup automático de dados

### SEO

- Meta tags otimizadas
- URLs amigáveis
- Sitemap automático
- Schema markup

## Próximos Passos

- **[Blog](blog.md)**: Sistema de blog
- **[Projetos](projects.md)**: Portfólio de projetos
- **[Representantes](representatives.md)**: Gestão de representantes 