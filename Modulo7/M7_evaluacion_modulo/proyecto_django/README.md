# Sistema de Gestión de Productos Django

Aplicación web desarrollada en Django 4.x conectada a PostgreSQL para la gestión de inventario.
Incluye relaciones de modelos complejas (1:1, 1:N, N:M) y operaciones CRUD completas.

## Características
- **CRUD Completo:** Productos, Categorías y Etiquetas.
- **Relaciones BD:**
  - Categoría -> Productos (1:N)
  - Producto <-> Etiquetas (N:M)
  - Producto -> Detalle (1:1)
- **Consultas Avanzadas:** Filtros por ORM y estadísticas con Raw SQL.
- **Seguridad:** Protección CSRF y autenticación de usuarios.
- **Frontend:** Estilizado con Bootstrap 5.

## Requisitos
- Python 3.8+
- PostgreSQL
- Django, Psycopg2

## Instalación

1. Clonar el repositorio.
2. Crear entorno virtual: `python -m venv venv`
3. Instalar dependencias: `pip install django psycopg2`
4. Configurar base de datos en `settings.py`.
5. Ejecutar migraciones:
   ```bash
   python manage.py makemigrations
   python manage.py migrate