clear

echo "Removendo arquivos de migração"
rm -rf db.sqlite3
rm -rf app/migrations
rm -rf blog/migrations
rm -rf projects/migrations
rm -rf representatives/migrations

echo "Criando migrações"
python manage.py makemigrations app
python manage.py makemigrations blog
python manage.py makemigrations projects
python manage.py makemigrations representatives

echo "Executando migrações"
python manage.py migrate

echo "Coletando arquivos estáticos"
python manage.py collectstatic --noinput

echo "Criando superusuário"
python manage.py createsuperuser

echo "Iniciando servidor"
python manage.py runserver