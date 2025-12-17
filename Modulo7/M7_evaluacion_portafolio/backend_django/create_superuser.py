# backend_django/create_superuser.py
import os
import django
from django.contrib.auth import get_user_model

# Configura el entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gestion_academica.settings')
django.setup()

User = get_user_model()
username = 'admin'
password = 'Admin1234'
email = 'admin@example.com'

if not User.objects.filter(username=username).exists():
    print(f"Creando superusuario: {username}...")
    User.objects.create_superuser(username, email, password)
    print("¡Superusuario creado con éxito!")
else:
    print("El superusuario ya existe. Omitiendo creación.")