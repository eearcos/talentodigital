#!/usr/bin/env bash
# exit on error
set -o errexit

# 1. Instalar dependencias
pip install -r requirements.txt

# 2. Recolectar archivos estáticos (CSS, imágenes)
python manage.py collectstatic --no-input

# 3. Crear las tablas en la base de datos (Migraciones)
python manage.py migrate

# 4. Cargar los cursos desde el JSON (Fixtures)
# Nota: Si modificaste el fixture, esto actualizará los datos.
python manage.py loaddata core/fixtures/cursos.json

# 5. Ejecutar el script para crear el admin
python create_superuser.py