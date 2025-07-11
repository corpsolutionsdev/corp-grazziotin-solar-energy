# Grazziotin Energia Solar - Documentação

Bem-vindo à documentação oficial do sistema Grazziotin Energia Solar! 🏠☀️

## Visão Geral

O sistema Grazziotin Energia Solar é uma aplicação web desenvolvida em Django para gerenciamento completo da empresa, incluindo:

- **Site Institucional**: Páginas principais da empresa
- **Blog**: Publicações e artigos técnicos
- **Projetos**: Portfólio de projetos realizados
- **Representantes**: Cadastro e gerenciamento de representantes
- **Painel Administrativo**: Interface completa para gestão de conteúdo

## 🚀 Início Rápido

```bash
# Clone o repositório
git clone https://github.com/corpsolutionsdev/corp-grazziotin-solar-energy.git
cd corp-grazziotin-solar-energy

# Configure o ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows

# Instale as dependências
pip install -r requirements.txt

# Execute as migrações
python manage.py migrate

# Inicie o servidor
python manage.py runserver
```

Acesse: [http://localhost:8000](http://localhost:8000)

## 📋 Pré-requisitos

- Python 3.8+
- Django 5.2+
- SQLite (desenvolvimento) / PostgreSQL (produção)
- Git

## 🏗️ Estrutura do Projeto

```
corp-grazziotin-solar-energy/
├── app/                    # Módulo principal
│   ├── models.py          # Modelos: QuemSomos, Contato
│   ├── views.py           # Views principais
│   └── urls.py            # URLs do app principal
├── blog/                   # Sistema de blog
│   ├── models.py          # Modelo: Artigo
│   ├── views.py           # Views do blog
│   └── urls.py            # URLs do blog
├── projects/               # Sistema de projetos
│   ├── models.py          # Modelo: Projeto
│   ├── views.py           # Views dos projetos
│   └── urls.py            # URLs dos projetos
├── representatives/        # Sistema de representantes
│   ├── models.py          # Modelo: Representante
│   └── views.py           # Views dos representantes
├── core/                   # Configurações Django
│   ├── settings.py        # Configurações do projeto
│   ├── urls.py            # URLs principais
│   └── wsgi.py            # Configuração WSGI
├── static/                 # Arquivos estáticos
│   ├── css/               # Folhas de estilo
│   ├── js/                # JavaScript
│   └── images/            # Imagens
├── templates/              # Templates HTML
├── manage.py              # Gerenciador Django
└── requirements.txt       # Dependências Python
```

## 🔧 Funcionalidades Principais

### Site Institucional
- Página inicial responsiva
- Seção "Quem Somos"
- Formulário de contato
- Design moderno e profissional

### Blog
- Sistema completo de blog
- Editor rico para artigos
- Categorização de conteúdo
- SEO otimizado

### Projetos
- Portfólio de projetos
- Galeria de imagens
- Detalhes técnicos
- Filtros por categoria

### Representantes
- Cadastro de representantes
- Informações de contato
- Área de atuação
- Gestão territorial

### Painel Administrativo
- Interface Django Admin customizada
- Gerenciamento de conteúdo
- Upload de imagens
- Controle de usuários

## 📚 Documentação

Esta documentação está organizada nas seguintes seções:

- **[Guia de Instalação](installation/installation.md)**: Como configurar o ambiente
- **[Desenvolvimento](development/project-structure.md)**: Estrutura e desenvolvimento
- **[Módulos](modules/app.md)**: Documentação dos módulos
- **[Admin](admin/dashboard.md)**: Painel administrativo
- **[Deploy](deploy/production.md)**: Configuração de produção
- **[Contribuição](contributing/contributing.md)**: Como contribuir

## 🎨 Tecnologias Utilizadas

- **Backend**: Django 5.2
- **Frontend**: HTML5, CSS3, JavaScript
- **Banco de Dados**: SQLite (dev) / PostgreSQL (prod)
- **Servidor**: Gunicorn + Nginx
- **Documentação**: MkDocs + Material Theme

## 🤝 Contribuição

Contribuições são bem-vindas! Consulte nossa [guia de contribuição](contributing/contributing.md) para mais detalhes.

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

---

**Grazziotin Energia Solar** - Energia solar para um futuro sustentável! ☀️🌱
