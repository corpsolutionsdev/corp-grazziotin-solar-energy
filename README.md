# Grazziotin Energia Solar

[![Documentação](https://img.shields.io/badge/Documentação-MkDocs%20Material-orange?logo=readthedocs&style=flat)](https://grazziotin-solar-energy.com)

Sistema web completo para gerenciamento da empresa Grazziotin Energia Solar, desenvolvido em Django. Inclui site institucional, blog, portfólio de projetos, cadastro de representantes e painel administrativo.

## 🚀 Visão Geral

- **Site Institucional**: Páginas principais da empresa
- **Blog**: Publicações e artigos técnicos
- **Projetos**: Portfólio de projetos realizados
- **Representantes**: Cadastro e gerenciamento de representantes
- **Painel Administrativo**: Interface completa para gestão de conteúdo

## 📚 Documentação

Acesse a documentação completa, com guias de instalação, desenvolvimento, módulos, deploy e contribuição:

👉 [https://grazziotin-solar-energy.com](https://grazziotin-solar-energy.com)

## 📋 Pré-requisitos

- Python 3.8+
- Django 5.2+
- pip
- Git

## 🔧 Instalação Rápida

```bash
# Clone o repositório
git clone https://github.com/corpsolutionsdev/corp-grazziotin-solar-energy.git
cd corp-grazziotin-solar-energy

# Crie o ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate   # Windows

# Instale as dependências
pip install -r requirements.txt

# Execute as migrações
python manage.py migrate

# Crie um superusuário
python manage.py createsuperuser

# Inicie o servidor
django-admin runserver
```

Acesse: [http://localhost:8000](http://localhost:8000)

## 🚢 Deploy com Docker

Você pode rodar todo o sistema em containers usando Docker e docker-compose, incluindo Django + Gunicorn, PostgreSQL e Nginx.

### 1. Crie um arquivo `.env` na raiz do projeto:

```bash
# Copie o arquivo de exemplo
cp env.deploy.example .env

# Edite as variáveis conforme necessário
nano .env
```

Exemplo de configuração básica:

```env
DJANGO_SECRET_KEY=sua-chave-secreta-muito-segura
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
DJANGO_DB_HOST=db
DJANGO_DB_NAME=grazziotin_db
DJANGO_DB_USER=grazziotin_user
DJANGO_DB_PASSWORD=grazziotin_pass
DEBUG=0
```

### 2. Suba os containers:

```bash
docker-compose up --build
```

- O serviço web (Django + Gunicorn) estará disponível em http://localhost
- O Nginx faz proxy reverso e serve arquivos estáticos
- O banco de dados PostgreSQL é iniciado automaticamente

### 3. Comandos úteis

- Parar os containers:
  ```bash
  docker-compose down
  ```
- Aplicar migrações:
  ```bash
  docker-compose exec web python manage.py migrate
  ```
- Criar superusuário:
  ```bash
  docker-compose exec web python manage.py createsuperuser
  ```
- Coletar estáticos (se necessário):
  ```bash
  docker-compose exec web python manage.py collectstatic --noinput
  ```

### 4. Estrutura dos serviços

- **web**: Django + Gunicorn
- **db**: PostgreSQL
- **nginx**: Proxy reverso e arquivos estáticos

Acesse o sistema em: [http://localhost](http://localhost)

## 🏗️ Estrutura do Projeto

```
corp-grazziotin-solar-energy/
├── app/                    # Módulo principal
├── blog/                   # Sistema de blog
├── projects/               # Sistema de projetos
├── representatives/        # Sistema de representantes
├── core/                   # Configurações Django
├── static/                 # Arquivos estáticos
├── templates/              # Templates HTML
├── manage.py               # Gerenciador Django
└── requirements.txt        # Dependências Python
```

## 🔑 Funcionalidades Principais

- Página inicial responsiva
- Seção "Quem Somos"
- Formulário de contato
- Blog completo
- Portfólio de projetos
- Cadastro de representantes
- Painel administrativo (Django Admin)
- Upload de imagens
- Controle de usuários

## 🎨 Tecnologias Utilizadas

- **Backend**: Django 5.2
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap
- **Banco de Dados**: SQLite (dev) / PostgreSQL (prod)
- **Servidor**: Gunicorn + Nginx
- **Documentação**: MkDocs + Material Theme

## 🤝 Contribuição

Contribuições são bem-vindas! Consulte o [guia de contribuição](https://grazziotin-solar-energy.com/contributing/contributing/) para mais detalhes.

1. Fork o projeto
2. Crie uma branch para sua feature
3. Commit suas mudanças
4. Push para a branch
5. Abra um Pull Request

## 📞 Contato

**Grazziotin Energia Solar**
- **Endereço**: R. Manoel Furtado Neves, 895 - Centro, São Mateus do Sul - PR, 83900-000
- **Telefones**: (42) 99975-1219 | (42) 99803-5252
- **Email**: contato@grazziotinenergiasolar.com.br
- **Horário**: De Segunda a Sexta das 9h às 18h

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

---

**Grazziotin Energia Solar** - Energia solar para um futuro sustentável! ☀️🌱 