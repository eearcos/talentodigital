# Sistema de Gestión Interno - Growth Academy (Python) 🐍

Hola! Esta es la parte lógica de mi proyecto **Growth Academy**.

Además de la página web, desarrollé este script de consola (CLI) para simular cómo funcionaría el sistema administrativo por detrás. Sirve para que el equipo pueda registrar alumnos, calcular precios con descuentos y revisar notas, aplicando toda la lógica de programación que aprendí en el módulo.

## 💡 ¿Qué hace este programa?

El archivo `sistema_gestion.py` incluye un menú interactivo con las siguientes opciones:

1.  **Registrar Alumnos:** Pide datos como nombre, edad y beca, y los guarda temporalmente en una lista.
2.  **Catálogo de Cursos:** Recorre la base de datos (diccionario) y muestra qué cursos ofrecemos y sus precios.
3.  **Cotizador Inteligente:** Calcula el precio final de un curso aplicando lógica de descuentos automática (si eres muy joven o tercera edad, pagas menos).
4.  **Verificador de Notas:** Pides las notas de los módulos, calcula el promedio y el sistema decide si el alumno aprueba o reprueba.

## 🛠️ Conceptos Técnicos Aplicados

En este código implementé los requerimientos funcionales del lenguaje Python:

* **Tipos de Datos:** Uso `int` para cálculos, `float` para los promedios de notas y `strings` para los textos.
* **Estructuras de Datos:**
    * Uso **Diccionarios** para mapear los cursos con sus precios.
    * Uso **Listas** para ir guardando el registro de alumnos nuevos.
* **Condicionales (`if/elif/else`):** Son el cerebro del programa. Los uso para validar la edad en los descuentos y para definir la aprobación (nota >= 4.0).
* **Bucles (`Loops`):**
    * `While True`: Para mantener el menú principal abierto hasta que el usuario decida salir.
    * `For`: Para iterar sobre los cursos disponibles y mostrarlos en pantalla.
* **Funciones:** Dividí el problema en partes pequeñas (funciones) para no repetir código y mantenerlo ordenado.

## 🚀 Cómo ejecutarlo

Para probar el script, solo necesitas tener Python instalado en tu equipo.

1. Abre la terminal y entra a esta carpeta:
   ```bash
   cd backend_python