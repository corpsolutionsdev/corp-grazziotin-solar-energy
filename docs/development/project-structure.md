# Estrutura do Projeto

Esta página descreve a estrutura completa do projeto Grazziotin Energia Solar.

## Visão Geral

O projeto segue a arquitetura padrão do Django com múltiplos apps, cada um responsável por uma funcionalidade específica.

## Estrutura de Diretórios

```
corp-grazziotin-solar-energy/
├── app/                    # App principal - Site institucional
│   ├── __init__.py
│   ├── admin.py           # Configuração do admin
│   ├── apps.py            # Configuração do app
│   ├── models.py          # Modelos: QuemSomos, Contato
│   ├── migrations/        # Migrações do banco
│   ├── tests.py           # Testes unitários
│   ├── urls.py            # URLs do app
│   └── views.py           # Views principais
├── blog/                   # Sistema de blog
│   ├── __init__.py
│   ├── admin.py           # Admin do blog
│   ├── apps.py
│   ├── models.py          # Modelo: Artigo
│   ├── migrations/
│   ├── tests.py
│   ├── urls.py            # URLs do blog
│   └── views.py           # Views do blog
├── projects/               # Sistema de projetos
│   ├── __init__.py
│   ├── admin.py           # Admin dos projetos
│   ├── apps.py
│   ├── models.py          # Modelo: Projeto
│   ├── migrations/
│   ├── tests.py
│   ├── urls.py            # URLs dos projetos
│   └── views.py           # Views dos projetos
├── representatives/        # Sistema de representantes
│   ├── __init__.py
│   ├── admin.py           # Admin dos representantes
│   ├── apps.py
│   ├── models.py          # Modelo: Representante
│   ├── migrations/
│   ├── tests.py
│   └── views.py           # Views dos representantes
├── core/                   # Configurações do projeto
│   ├── __init__.py
│   ├── settings.py        # Configurações Django
│   ├── urls.py            # URLs principais
│   ├── wsgi.py            # Configuração WSGI
│   └── asgi.py            # Configuração ASGI
├── static/                 # Arquivos estáticos
│   ├── css/
│   │   ├── base.css       # Estilos base
│   │   └── custom_admin.css # Estilos do admin
│   ├── js/
│   │   └── main.js        # JavaScript principal
│   └── images/
│       ├── logo.png        # Logo da empresa
│       ├── background.jpg  # Imagem de fundo
│       └── illustrations/  # Ilustrações SVG
├── templates/              # Templates HTML
│   ├── base.html          # Template base
│   ├── 404.html           # Página de erro
│   ├── app/               # Templates do app principal
│   │   ├── home.html      # Página inicial
│   │   ├── contato.html   # Página de contato
│   │   └── quem_somos.html # Página institucional
│   ├── blog/              # Templates do blog
│   │   ├── blog.html      # Lista de artigos
│   │   └── artigo_detalhe.html # Detalhe do artigo
│   └── projects/          # Templates dos projetos
│       ├── projetos.html  # Lista de projetos
│       └── projeto_detalhe.html # Detalhe do projeto
├── manage.py              # Gerenciador Django
├── requirements.txt        # Dependências Python
├── README.md              # Documentação do projeto
└── .gitignore             # Arquivos ignorados pelo Git
```

## Apps Django

### App Principal (`app/`)

Responsável pelas páginas institucionais da empresa.

**Modelos:**
- `QuemSomos`: Informações sobre a empresa
- `Contato`: Mensagens recebidas via formulário

**Views:**
- `home`: Página inicial
- `quem_somos`: Página institucional
- `contato`: Formulário de contato

### Blog (`blog/`)

Sistema completo de blog para publicações técnicas.

**Modelos:**
- `Artigo`: Posts do blog com título, conteúdo, data, etc.

**Views:**
- `blog`: Lista de artigos
- `artigo_detalhe`: Visualização individual do artigo

### Projetos (`projects/`)

Portfólio de projetos realizados pela empresa.

**Modelos:**
- `Projeto`: Projetos com detalhes técnicos e imagens

**Views:**
- `projetos`: Lista de projetos
- `projeto_detalhe`: Detalhes do projeto

### Representantes (`representatives/`)

Sistema de cadastro e gerenciamento de representantes.

**Modelos:**
- `Representante`: Dados dos representantes da empresa

**Views:**
- `representantes`: Lista de representantes

## Configurações (`core/`)

### settings.py

Principais configurações:

```python
# Apps instalados
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',
    'blog',
    'projects',
    'representatives',
]

# Configurações de idioma
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'

# Arquivos estáticos
STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Configurações de email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
```

### urls.py

Configuração das URLs principais:

```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('blog/', include('blog.urls')),
    path('projects/', include('projects.urls')),
]
```

## Arquivos Estáticos

### CSS (`static/css/`)

- `base.css`: Estilos base do site
- `custom_admin.css`: Personalização do painel admin

### JavaScript (`static/js/`)

- `main.js`: Funcionalidades JavaScript principais

### Imagens (`static/images/`)

- `logo.png`: Logo da empresa
- `background.jpg`: Imagem de fundo
- `illustrations/`: Ilustrações SVG do site

## Templates

### Template Base (`templates/base.html`)

Template principal que define a estrutura HTML comum a todas as páginas.

**Características:**
- Meta tags para SEO
- Inclusão de CSS e JavaScript
- Menu de navegação
- Footer com informações da empresa

### Templates Específicos

Cada app tem seus próprios templates organizados em subdiretórios:

- `app/`: Templates das páginas institucionais
- `blog/`: Templates do sistema de blog
- `projects/`: Templates do portfólio de projetos

## Banco de Dados

### SQLite (Desenvolvimento)

Arquivo `db.sqlite3` na raiz do projeto.

### Migrações

Cada app possui sua pasta `migrations/` com arquivos de migração do Django.

## Configuração de Ambiente

### Variáveis de Ambiente

O projeto usa `python-dotenv` para carregar configurações do arquivo `.env`:

```bash
SECRET_KEY=sua-chave-secreta
DEBUG=True
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1
EMAIL_HOST_USER=seu-email@gmail.com
EMAIL_HOST_PASSWORD=sua-senha-de-app
```

## Próximos Passos

- **[Configurações](settings.md)**: Detalhes das configurações Django
- **[Modelos](models.md)**: Documentação dos modelos de dados
- **[Views](views.md)**: Documentação das views
- **[Templates](templates.md)**: Guia dos templates HTML 