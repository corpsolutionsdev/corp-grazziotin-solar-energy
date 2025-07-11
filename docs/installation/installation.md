# Instalação

Este guia irá ajudá-lo a configurar o ambiente de desenvolvimento para o sistema Grazziotin Energia Solar.

## Pré-requisitos

Antes de começar, certifique-se de ter instalado:

- **Python 3.8+**: [Download Python](https://www.python.org/downloads/)
- **Git**: [Download Git](https://git-scm.com/downloads)
- **pip**: Gerenciador de pacotes Python (vem com Python)

## Passo a Passo

### 1. Clone o Repositório

```bash
git clone https://github.com/corpsolutionsdev/corp-grazziotin-solar-energy.git
cd corp-grazziotin-solar-energy
```

### 2. Configure o Ambiente Virtual

```bash
# Crie o ambiente virtual
python -m venv venv

# Ative o ambiente virtual
# Linux/Mac:
source venv/bin/activate

# Windows:
venv\Scripts\activate
```

### 3. Instale as Dependências

```bash
pip install -r requirements.txt
```

### 4. Configure as Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto:

```bash
# Configurações do Django
SECRET_KEY=sua-chave-secreta-aqui
DEBUG=True
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1

# Configurações de Email (opcional)
EMAIL_HOST_USER=seu-email@gmail.com
EMAIL_HOST_PASSWORD=sua-senha-de-app
```

### 5. Execute as Migrações

```bash
python manage.py migrate
```

### 6. Crie um Superusuário (Opcional)

```bash
python manage.py createsuperuser
```

### 7. Inicie o Servidor

```bash
python manage.py runserver
```

Acesse: [http://localhost:8000](http://localhost:8000)

## Verificação da Instalação

Para verificar se tudo está funcionando:

1. Acesse [http://localhost:8000](http://localhost:8000)
2. Você deve ver a página inicial do sistema
3. Acesse [http://localhost:8000/admin](http://localhost:8000/admin) para o painel administrativo

## Solução de Problemas

### Erro: "No module named 'django'"
```bash
# Certifique-se de que o ambiente virtual está ativo
source venv/bin/activate
pip install -r requirements.txt
```

### Erro: "ModuleNotFoundError: No module named 'dotenv'"
```bash
pip install python-dotenv
```

### Erro: "Database is locked"
```bash
# Pare o servidor e tente novamente
python manage.py migrate
```

### Erro: "Port 8000 is already in use"
```bash
# Use uma porta diferente
python manage.py runserver 8001
```

## Próximos Passos

Após a instalação bem-sucedida:

1. **[Configuração](configuration.md)**: Configure o sistema para seu ambiente
2. **[Desenvolvimento](development/project-structure.md)**: Entenda a estrutura do projeto
3. **[Admin](admin/dashboard.md)**: Aprenda a usar o painel administrativo

## Suporte

Se encontrar problemas durante a instalação:

- Verifique se todos os pré-requisitos estão instalados
- Certifique-se de que o ambiente virtual está ativo
- Consulte os logs de erro para mais detalhes
- Abra uma issue no GitHub se o problema persistir 