web: cd backend && gunicorn website.wsgi
release: cd backend && python manage.py makemigrations && python manage.py makemigrations inventory && python manage.py migrate && python manage.py migrate inventory