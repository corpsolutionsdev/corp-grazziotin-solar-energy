# Configuração

Após a instalação, você precisa configurar o ambiente para desenvolvimento e produção.

## Configuração de Desenvolvimento

### 1. Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto:

```bash
# Configurações do Django
SECRET_KEY=sua-chave-secreta-aqui-para-desenvolvimento
DEBUG=True
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]

# Configurações de Email (opcional)
EMAIL_HOST_USER=seu-email@gmail.com
EMAIL_HOST_PASSWORD=sua-senha-de-app-gmail

# Configurações de Banco de Dados (opcional)
DATABASE_URL=sqlite:///db.sqlite3
```

### 2. Configurações do Django

O arquivo `core/settings.py` já está configurado para desenvolvimento:

```python
# Configurações de idioma
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'

# Configurações de arquivos estáticos
STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Configurações de mídia
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

### 3. Banco de Dados

Para desenvolvimento, o SQLite é usado por padrão:

```bash
# Executar migrações
python manage.py migrate

# Criar superusuário
python manage.py createsuperuser
```

## Configuração de Produção

### 1. Variáveis de Ambiente

```bash
# Configurações de Produção
SECRET_KEY=chave-secreta-muito-segura-para-producao
DEBUG=False
DJANGO_ALLOWED_HOSTS=seudominio.com www.seudominio.com

# Configurações de Email
EMAIL_HOST_USER=contato@seudominio.com
EMAIL_HOST_PASSWORD=senha-segura-do-email

# Configurações de Banco de Dados
DATABASE_URL=postgresql://usuario:senha@localhost:5432/grazziotin_db
```

### 2. Banco de Dados PostgreSQL

```bash
# Instalar PostgreSQL
sudo apt install postgresql postgresql-contrib

# Criar banco de dados
sudo -u postgres psql
CREATE DATABASE grazziotin_db;
CREATE USER grazziotin_user WITH PASSWORD 'senha-segura';
GRANT ALL PRIVILEGES ON DATABASE grazziotin_db TO grazziotin_user;
\q
```

### 3. Configurações de Segurança

```python
# settings.py para produção
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
```

## Configuração de Email

### Gmail SMTP

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'seu-email@gmail.com'
EMAIL_HOST_PASSWORD = 'sua-senha-de-app'
```

### Configurar Senha de App Gmail

1. Acesse [myaccount.google.com](https://myaccount.google.com)
2. Vá em "Segurança"
3. Ative a verificação em duas etapas
4. Gere uma senha de app
5. Use essa senha no `EMAIL_HOST_PASSWORD`

## Configuração de Logs

### Desenvolvimento

```python
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
}
```

### Produção

```python
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': '/var/log/grazziotin/django.log',
            'formatter': 'verbose',
        },
    },
    'root': {
        'handlers': ['file'],
        'level': 'INFO',
    },
}
```

## Configuração de Cache

### Redis (Recomendado)

```bash
# Instalar Redis
sudo apt install redis-server

# Instalar dependência Python
pip install redis
```

```python
# settings.py
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
    }
}
```

## Configuração de Arquivos Estáticos

### Desenvolvimento

```bash
# Coletar arquivos estáticos
python manage.py collectstatic
```

### Produção (Nginx)

```nginx
# /etc/nginx/sites-available/grazziotin
server {
    listen 80;
    server_name seudominio.com;

    location /static/ {
        alias /path/to/project/staticfiles/;
    }

    location /media/ {
        alias /path/to/project/media/;
    }

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

## Configuração de Monitoramento

### Sentry (Opcional)

```bash
pip install sentry-sdk
```

```python
# settings.py
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

sentry_sdk.init(
    dsn="sua-dsn-do-sentry",
    integrations=[DjangoIntegration()],
    traces_sample_rate=1.0,
    send_default_pii=True,
)
```

## Verificação da Configuração

### Teste de Configuração

```bash
# Verificar configurações
python manage.py check

# Testar conexão com banco
python manage.py dbshell

# Testar envio de email
python manage.py shell
>>> from django.core.mail import send_mail
>>> send_mail('Teste', 'Mensagem de teste', 'from@example.com', ['to@example.com'])
```

## Próximos Passos

Após configurar o ambiente:

1. **[Desenvolvimento](development/project-structure.md)**: Entenda a estrutura
2. **[Admin](admin/dashboard.md)**: Configure o painel administrativo
3. **[Deploy](deploy/production.md)**: Prepare para produção

## Solução de Problemas

### Erro de Conexão com Banco

```bash
# Verificar se PostgreSQL está rodando
sudo systemctl status postgresql

# Reiniciar PostgreSQL
sudo systemctl restart postgresql
```

### Erro de Permissão de Arquivos

```bash
# Ajustar permissões
sudo chown -R www-data:www-data /path/to/project
sudo chmod -R 755 /path/to/project
```

### Erro de Email

- Verifique se a senha de app está correta
- Confirme se a verificação em duas etapas está ativa
- Teste com outro provedor de email 