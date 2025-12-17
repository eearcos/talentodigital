-- POBLAMIENTO DE DATOS (SEEDS)

-- Insertar Estudiantes
INSERT INTO Estudiantes (nombre, apellido, email) VALUES 
('Juan', 'Pérez', 'juan.perez@email.com'),
('Maria', 'Gomez', 'maria.gomez@email.com'),
('Carlos', 'Ruiz', 'carlos.ruiz@email.com');

-- Insertar Cursos
INSERT INTO Cursos (nombre_curso, precio, instructor) VALUES 
('Ecommerce Master', 150000, 'Esteban Arcos'),
('Growth Marketing', 120000, 'Ana Lopez'),
('Ads Avanzado', 90000, 'Pedro Diaz');

-- Insertar Inscripciones (Simulando compras)
-- Juan se inscribe en Ecommerce
INSERT INTO Inscripciones (id_estudiante, id_curso, fecha_inscripcion) VALUES (1, 1, '2023-10-01');
-- Maria se inscribe en Growth
INSERT INTO Inscripciones (id_estudiante, id_curso, fecha_inscripcion) VALUES (2, 2, '2023-10-02');
-- Juan se inscribe TAMBIÉN en Ads (Un alumno, varios cursos)
INSERT INTO Inscripciones (id_estudiante, id_curso, fecha_inscripcion) VALUES (1, 3, '2023-10-05');