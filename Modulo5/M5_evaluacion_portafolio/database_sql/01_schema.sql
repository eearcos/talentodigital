-- ESQUEMA DE BASE DE DATOS - GROWTH ACADEMY

-- 1. Tabla de Estudiantes
CREATE TABLE Estudiantes (
    id_estudiante INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    fecha_registro DATE DEFAULT CURRENT_DATE
);

-- 2. Tabla de Cursos
CREATE TABLE Cursos (
    id_curso INT PRIMARY KEY AUTO_INCREMENT,
    nombre_curso VARCHAR(100) NOT NULL,
    precio DECIMAL(10, 2) NOT NULL,
    instructor VARCHAR(50)
);

-- 3. Tabla de Inscripciones (Relación Muchos a Muchos)
-- Relaciona Estudiantes con Cursos mediante Claves Foráneas (FK)
CREATE TABLE Inscripciones (
    id_inscripcion INT PRIMARY KEY AUTO_INCREMENT,
    id_estudiante INT,
    id_curso INT,
    fecha_inscripcion DATE,
    FOREIGN KEY (id_estudiante) REFERENCES Estudiantes(id_estudiante),
    FOREIGN KEY (id_curso) REFERENCES Cursos(id_curso)
);