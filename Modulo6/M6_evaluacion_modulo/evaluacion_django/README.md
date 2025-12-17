# Gestor de Tareas - Evaluación Django

Este proyecto es una aplicación web desarrollada con Django que permite a los usuarios gestionar una lista de tareas personales. El sistema implementa un flujo completo de autenticación y manejo de datos en memoria para las tareas.

## 🚀 Funcionalidades Principales

1.  **Autenticación de Usuarios:**
    * Registro de nuevos usuarios.
    * Inicio de sesión (Login) y Cierre de sesión (Logout).
    * Protección de rutas: Solo usuarios autenticados pueden acceder al sistema.

2.  **Gestión de Tareas (CRUD en Memoria):**
    * **Crear:** Los usuarios pueden agregar nuevas tareas mediante formularios.
    * **Leer:** Visualización de lista de tareas y detalles individuales.
    * **Eliminar:** Opción para borrar tareas específicas.
    * *Nota técnica:* Las tareas se almacenan en una lista global en memoria (`TAREAS = []`) dentro de `views.py`, simulando una base de datos volátil.

3.  **Privacidad y Seguridad:**
    * Aislamiento de datos: Cada usuario visualiza y gestiona únicamente sus propias tareas.
    * Validación de permisos en las vistas de detalle y eliminación.

4.  **Interfaz Gráfica:**
    * Diseño responsivo implementado con **Bootstrap 5**.
    * Plantillas HTML personalizadas y traducidas al español.

## 📂 Estructura del Proyecto

El proyecto sigue la arquitectura MVT (Modelo-Vista-Template) de Django:

* **`gestor_tareas/`**: Configuración global (`settings.py`, `urls.py`).
* **`tareas/`**: Aplicación principal.
    * `views.py`: Contiene la lógica de negocio, la lista en memoria `TAREAS` y las vistas protegidas con `@login_required`.
    * `forms.py`: Definición del formulario `TareaForm` usando Django Forms.
    * `urls.py`: Rutas específicas de la aplicación.
    * `templates/tareas/`: Archivos HTML para el flujo de tareas (`lista.html`, `detalle.html`, etc.).
    * `templates/registration/`: Archivos HTML para Login y Registro.

## ⚙️ Instrucciones de Instalación y Ejecución

Sigue estos pasos para ejecutar el proyecto en tu entorno local.

### 1. Configurar el Entorno Virtual

Abre tu terminal en la carpeta del proyecto y crea el entorno:

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate