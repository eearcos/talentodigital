-- CONSULTAS Y MANIPULACIÓN DE DATOS

-- 1. CONSULTA CON JOIN (Obtener qué cursos compró Juan Pérez)
SELECT e.nombre, e.apellido, c.nombre_curso, c.precio
FROM Inscripciones i
JOIN Estudiantes e ON i.id_estudiante = e.id_estudiante
JOIN Cursos c ON i.id_curso = c.id_curso
WHERE e.nombre = 'Juan';

-- 2. ACTUALIZACIÓN DE DATOS (UPDATE)
-- Subir el precio del curso de Growth Marketing
UPDATE Cursos 
SET precio = 130000 
WHERE nombre_curso = 'Growth Marketing';

-- 3. ELIMINACIÓN DE DATOS (DELETE)
-- Borrar al estudiante Carlos Ruiz porque se dio de baja
DELETE FROM Estudiantes WHERE email = 'carlos.ruiz@email.com';

-- 4. AGRUPACIÓN (GROUP BY)
-- Contar cuántos alumnos hay por curso
SELECT c.nombre_curso, COUNT(i.id_inscripcion) as total_alumnos
FROM Cursos c
LEFT JOIN Inscripciones i ON c.id_curso = i.id_curso
GROUP BY c.nombre_curso;