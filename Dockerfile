# Dockerfile para Grazziotin Energia Solar
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Instala dependências do sistema
RUN apt-get update && \
    apt-get install -y build-essential libpq-dev && \
    rm -rf /var/lib/apt/lists/*

# Instala dependências Python
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copia o projeto
COPY . .

# Coleta arquivos estáticos
RUN python manage.py collectstatic --noinput

# Expõe a porta padrão do Gunicorn
EXPOSE 8000

# Comando de inicialização
CMD ["gunicorn", "core.wsgi:application", "--bind", "0.0.0.0:8000"] 