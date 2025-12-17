# Módulo de Base de Datos SQL 🗄️

Este directorio contiene los scripts SQL necesarios para gestionar la persistencia de datos de **Growth Academy**.

## 🧠 Conceptos de Base de Datos Relacional

Para este proyecto, utilizamos una base de datos relacional porque necesitamos consistencia y relacionar datos entre sí. Sus componentes principales son:

1.  **Tablas:** Estructuras donde guardamos los datos (ej: `Estudiantes`).
2.  **Registros (Filas):** Cada unidad de información (ej: un estudiante específico).
3.  **Campos (Columnas):** Los atributos del dato (ej: `email`, `precio`).
4.  **Clave Primaria (PK):** Identificador único (ej: `id_estudiante`). No se repite.
5.  **Clave Foránea (FK):** Campo que conecta dos tablas. En la tabla `Inscripciones`, usamos `id_estudiante` para saber quién compró el curso.

## 📂 Archivos del Repositorio

1.  **`01_schema.sql` (DDL):** Contiene los comandos `CREATE TABLE`. Define la estructura y las reglas de integridad.
2.  **`02_seeds.sql` (DML):** Contiene los `INSERT` para poblar la base de datos con información inicial de prueba.
3.  **`03_queries.sql` (Queries):** Contiene ejemplos de:
    * `SELECT` con `JOIN` para cruzar tablas.
    * `UPDATE` para modificar precios.
    * `DELETE` para eliminar registros.

## 🚀 Cómo ejecutar
Estos archivos son scripts estándar SQL. Pueden ejecutarse en cualquier motor de base de datos como MySQL, PostgreSQL o SQLite.