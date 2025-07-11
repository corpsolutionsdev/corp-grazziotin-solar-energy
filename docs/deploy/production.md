# Deploy em Produção

Guia completo para fazer o deploy do sistema Grazziotin Energia Solar em ambiente de produção.

## Pré-requisitos

### Servidor

- **Sistema Operacional**: Ubuntu 20.04+ ou CentOS 8+
- **RAM**: Mínimo 2GB (recomendado 4GB+)
- **CPU**: 2 cores (recomendado 4+)
- **Disco**: 20GB+ de espaço livre

### Software Necessário

```bash
# Atualizar sistema
sudo apt update && sudo apt upgrade -y

# Instalar dependências
sudo apt install python3 python3-pip python3-venv nginx postgresql postgresql-contrib redis-server git curl
```

## 🚢 Deploy com Docker (Recomendado)

A forma mais simples e eficiente de fazer deploy é usando Docker e docker-compose, que inclui todos os serviços necessários.

### 1. Instalar Docker e Docker Compose

```bash
# Instalar Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# Adicionar usuário ao grupo docker
sudo usermod -aG docker $USER

# Instalar Docker Compose
sudo curl -L "https://github.com/docker/compose/releases/download/v2.20.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

# Reiniciar sessão para aplicar grupo docker
newgrp docker
```

### 2. Configurar Variáveis de Ambiente

```bash
# Criar arquivo .env para produção
cat > .env << EOF
DJANGO_SECRET_KEY=sua-chave-secreta-muito-segura-para-producao
DJANGO_ALLOWED_HOSTS=seudominio.com www.seudominio.com
DJANGO_DB_HOST=db
DJANGO_DB_NAME=grazziotin_db
DJANGO_DB_USER=grazziotin_user
DJANGO_DB_PASSWORD=senha-segura-para-producao
DEBUG=0
EMAIL_HOST_USER=contato@seudominio.com
EMAIL_HOST_PASSWORD=sua-senha-de-app
EOF
```

### 3. Deploy dos Containers

```bash
# Clonar projeto
git clone https://github.com/corpsolutionsdev/corp-grazziotin-solar-energy.git
cd corp-grazziotin-solar-energy

# Subir containers em background
docker-compose up -d --build

# Verificar status
docker-compose ps
```

### 4. Configuração Inicial

```bash
# Executar migrações
docker-compose exec web python manage.py migrate

# Criar superusuário
docker-compose exec web python manage.py createsuperuser

# Coletar arquivos estáticos
docker-compose exec web python manage.py collectstatic --noinput
```

### 5. Configurar Nginx para Produção

Atualize o arquivo `nginx.conf` para seu domínio:

```nginx
server {
    listen 80;
    server_name seudominio.com www.seudominio.com;

    # Arquivos estáticos
    location /static/ {
        alias /app/staticfiles/;
        expires 30d;
        add_header Cache-Control "public, immutable";
    }

    # Proxy para Gunicorn
    location / {
        proxy_pass http://web:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

### 6. SSL/HTTPS com Certbot

```bash
# Instalar certbot
sudo apt install certbot

# Obter certificado SSL
sudo certbot certonly --standalone -d seudominio.com -d www.seudominio.com

# Configurar Nginx com SSL
# (Adicionar configuração SSL ao nginx.conf)
```

### 7. Backup e Manutenção

```bash
# Backup do banco de dados
docker-compose exec db pg_dump -U grazziotin_user grazziotin_db > backup_$(date +%Y%m%d).sql

# Backup dos volumes
docker run --rm -v corp-grazziotin-solar-energy_postgres_data:/data -v $(pwd):/backup alpine tar czf /backup/postgres_backup_$(date +%Y%m%d).tar.gz -C /data .

# Restaurar backup
docker-compose exec -T db psql -U grazziotin_user grazziotin_db < backup_20240101.sql
```

### 8. Monitoramento

```bash
# Verificar logs
docker-compose logs -f web
docker-compose logs -f nginx
docker-compose logs -f db

# Verificar uso de recursos
docker stats

# Reiniciar serviços
docker-compose restart web
docker-compose restart nginx
```

### 9. Atualizações

```bash
# Script de atualização
cat > update-docker.sh << 'EOF'
#!/bin/bash
cd /path/to/corp-grazziotin-solar-energy

# Backup
docker-compose exec db pg_dump -U grazziotin_user grazziotin_db > backup_$(date +%Y%m%d).sql

# Atualizar código
git pull origin main

# Rebuild e restart
docker-compose down
docker-compose up -d --build

# Executar migrações
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py collectstatic --noinput
EOF

chmod +x update-docker.sh
```

### 10. Comandos Úteis

```bash
# Parar todos os serviços
docker-compose down

# Parar e remover volumes
docker-compose down -v

# Ver logs em tempo real
docker-compose logs -f

# Executar comando no container
docker-compose exec web python manage.py shell

# Backup completo
docker-compose exec db pg_dump -U grazziotin_user grazziotin_db | gzip > backup_$(date +%Y%m%d_%H%M%S).sql.gz
```

## Deploy Tradicional (Manual)

Se preferir fazer deploy sem Docker, siga as instruções abaixo. **Nota**: O deploy com Docker é recomendado por ser mais simples e consistente.

## Configuração do Servidor

### 1. Criar Usuário do Sistema

```bash
# Criar usuário para a aplicação
sudo adduser grazziotin
sudo usermod -aG sudo grazziotin

# Trocar para o usuário
su - grazziotin
```

### 2. Configurar SSH

```bash
# Gerar chave SSH
ssh-keygen -t rsa -b 4096 -C "seu-email@exemplo.com"

# Adicionar chave ao servidor
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
chmod 600 ~/.ssh/authorized_keys
```

### 3. Configurar Firewall

```bash
# Configurar UFW
sudo ufw allow ssh
sudo ufw allow 80
sudo ufw allow 443
sudo ufw enable
```

## Deploy da Aplicação

### 1. Clonar o Projeto

```bash
# Clonar repositório
git clone https://github.com/corpsolutionsdev/corp-grazziotin-solar-energy.git
cd corp-grazziotin-solar-energy

# Configurar ambiente virtual
python3 -m venv venv
source venv/bin/activate
```

### 2. Instalar Dependências

```bash
# Instalar dependências
pip install -r requirements.txt

# Instalar dependências de produção
pip install gunicorn psycopg2-binary redis
```

### 3. Configurar Variáveis de Ambiente

```bash
# Criar arquivo .env
cat > .env << EOF
SECRET_KEY=sua-chave-secreta-muito-segura-para-producao
DEBUG=False
DJANGO_ALLOWED_HOSTS=seudominio.com www.seudominio.com
EMAIL_HOST_USER=contato@seudominio.com
EMAIL_HOST_PASSWORD=sua-senha-de-app
DATABASE_URL=postgresql://grazziotin_user:senha@localhost:5432/grazziotin_db
EOF
```

### 4. Configurar Banco de Dados

```bash
# Acessar PostgreSQL
sudo -u postgres psql

# Criar banco e usuário
CREATE DATABASE grazziotin_db;
CREATE USER grazziotin_user WITH PASSWORD 'senha-segura';
GRANT ALL PRIVILEGES ON DATABASE grazziotin_db TO grazziotin_user;
\q

# Executar migrações
python manage.py migrate

# Criar superusuário
python manage.py createsuperuser
```

### 5. Configurar Arquivos Estáticos

```bash
# Coletar arquivos estáticos
python manage.py collectstatic

# Configurar permissões
sudo chown -R grazziotin:grazziotin /home/grazziotin/corp-grazziotin-solar-energy
sudo chmod -R 755 /home/grazziotin/corp-grazziotin-solar-energy
```

## Configuração do Gunicorn

### 1. Criar Arquivo de Configuração

```bash
# Criar arquivo de configuração
cat > gunicorn.conf.py << EOF
bind = "127.0.0.1:8000"
workers = 3
worker_class = "sync"
worker_connections = 1000
max_requests = 1000
max_requests_jitter = 50
timeout = 30
keepalive = 2
preload_app = True
EOF
```

### 2. Criar Serviço Systemd

```bash
# Criar arquivo de serviço
sudo tee /etc/systemd/system/grazziotin.service << EOF
[Unit]
Description=Grazziotin Energia Solar
After=network.target

[Service]
User=grazziotin
Group=grazziotin
WorkingDirectory=/home/grazziotin/corp-grazziotin-solar-energy
Environment="PATH=/home/grazziotin/corp-grazziotin-solar-energy/venv/bin"
ExecStart=/home/grazziotin/corp-grazziotin-solar-energy/venv/bin/gunicorn --config gunicorn.conf.py core.wsgi:application
ExecReload=/bin/kill -s HUP \$MAINPID
Restart=always

[Install]
WantedBy=multi-user.target
EOF

# Recarregar e habilitar serviço
sudo systemctl daemon-reload
sudo systemctl enable grazziotin
sudo systemctl start grazziotin
```

## Configuração do Nginx

### 1. Criar Configuração do Site

```bash
# Criar configuração do Nginx
sudo tee /etc/nginx/sites-available/grazziotin << EOF
server {
    listen 80;
    server_name seudominio.com www.seudominio.com;

    # Logs
    access_log /var/log/nginx/grazziotin_access.log;
    error_log /var/log/nginx/grazziotin_error.log;

    # Arquivos estáticos
    location /static/ {
        alias /home/grazziotin/corp-grazziotin-solar-energy/staticfiles/;
        expires 30d;
        add_header Cache-Control "public, immutable";
    }

    # Arquivos de mídia
    location /media/ {
        alias /home/grazziotin/corp-grazziotin-solar-energy/media/;
        expires 30d;
    }

    # Proxy para Gunicorn
    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host \$host;
        proxy_set_header X-Real-IP \$remote_addr;
        proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto \$scheme;
        proxy_redirect off;
    }
}
EOF

# Habilitar site
sudo ln -s /etc/nginx/sites-available/grazziotin /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

## Configuração de SSL (HTTPS)

### 1. Instalar Certbot

```bash
# Instalar Certbot
sudo apt install certbot python3-certbot-nginx

# Obter certificado SSL
sudo certbot --nginx -d seudominio.com -d www.seudominio.com
```

### 2. Configurar Renovação Automática

```bash
# Testar renovação automática
sudo certbot renew --dry-run

# Adicionar ao crontab
sudo crontab -e
# Adicionar linha: 0 12 * * * /usr/bin/certbot renew --quiet
```

## Monitoramento e Logs

### 1. Configurar Logs

```bash
# Criar diretório de logs
sudo mkdir -p /var/log/grazziotin
sudo chown grazziotin:grazziotin /var/log/grazziotin

# Configurar rotação de logs
sudo tee /etc/logrotate.d/grazziotin << EOF
/var/log/grazziotin/*.log {
    daily
    missingok
    rotate 52
    compress
    delaycompress
    notifempty
    create 644 grazziotin grazziotin
}
EOF
```

### 2. Monitoramento Básico

```bash
# Verificar status dos serviços
sudo systemctl status gunicorn
sudo systemctl status nginx
sudo systemctl status postgresql
sudo systemctl status redis

# Verificar logs
sudo journalctl -u grazziotin -f
sudo tail -f /var/log/nginx/grazziotin_error.log
```

## Backup e Manutenção

### 1. Backup do Banco de Dados

```bash
# Criar script de backup
cat > backup.sh << 'EOF'
#!/bin/bash
DATE=$(date +%Y%m%d_%H%M%S)
BACKUP_DIR="/home/grazziotin/backups"
mkdir -p $BACKUP_DIR

# Backup do banco
pg_dump grazziotin_db > $BACKUP_DIR/db_backup_$DATE.sql

# Backup dos arquivos de mídia
tar -czf $BACKUP_DIR/media_backup_$DATE.tar.gz media/

# Manter apenas últimos 7 backups
find $BACKUP_DIR -name "*.sql" -mtime +7 -delete
find $BACKUP_DIR -name "*.tar.gz" -mtime +7 -delete
EOF

chmod +x backup.sh

# Adicionar ao crontab
crontab -e
# Adicionar: 0 2 * * * /home/grazziotin/corp-grazziotin-solar-energy/backup.sh
```

### 2. Atualizações

```bash
# Script de atualização
cat > update.sh << 'EOF'
#!/bin/bash
cd /home/grazziotin/corp-grazziotin-solar-energy

# Backup antes da atualização
./backup.sh

# Atualizar código
git pull origin main

# Ativar ambiente virtual
source venv/bin/activate

# Instalar dependências
pip install -r requirements.txt

# Executar migrações
python manage.py migrate

# Coletar arquivos estáticos
python manage.py collectstatic --noinput

# Reiniciar serviços
sudo systemctl restart grazziotin
sudo systemctl reload nginx
EOF

chmod +x update.sh
```

## Verificação do Deploy

### 1. Testes Básicos

```bash
# Verificar se o site está acessível
curl -I http://seudominio.com

# Verificar SSL
curl -I https://seudominio.com

# Verificar arquivos estáticos
curl -I https://seudominio.com/static/css/base.css
```

### 2. Testes de Funcionalidade

- Acessar a página inicial
- Testar formulário de contato
- Verificar painel administrativo
- Testar upload de arquivos

## Solução de Problemas

### Erro 502 Bad Gateway

```bash
# Verificar se Gunicorn está rodando
sudo systemctl status grazziotin

# Verificar logs
sudo journalctl -u grazziotin -f

# Reiniciar serviço
sudo systemctl restart grazziotin
```

### Erro de Permissão

```bash
# Ajustar permissões
sudo chown -R grazziotin:grazziotin /home/grazziotin/corp-grazziotin-solar-energy
sudo chmod -R 755 /home/grazziotin/corp-grazziotin-solar-energy
```

### Erro de Banco de Dados

```bash
# Verificar conexão
sudo -u postgres psql -d grazziotin_db

# Verificar logs do PostgreSQL
sudo tail -f /var/log/postgresql/postgresql-*.log
```

## Próximos Passos

- **[Manutenção](maintenance.md)**: Guia de manutenção
- **[Monitoramento](monitoring.md)**: Configuração de monitoramento
- **[Backup](backup.md)**: Estratégias de backup 