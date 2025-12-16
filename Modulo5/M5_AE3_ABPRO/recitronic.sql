-- =========================================
-- RECITRONIC - Sistema de Reciclaje Electrónico
-- Base de datos: MySQL (InnoDB con transacciones ACID)
-- Ejercicio Grupal Completo
-- =========================================

-- 1. Crear base de datos y usarla
DROP DATABASE IF EXISTS recitronic;
CREATE DATABASE recitronic;
USE recitronic;

-- 2. Creación de tablas con PK AUTO_INCREMENT, FK y restricciones

CREATE TABLE Clientes (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    nombre     VARCHAR(100) NOT NULL,
    telefono   VARCHAR(50),
    direccion  VARCHAR(200)
) ENGINE=InnoDB;

CREATE TABLE Articulos (
    id_articulo  INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente   INT NOT NULL,
    tipo_articulo VARCHAR(100) NOT NULL,
    estado        VARCHAR(50)  NOT NULL DEFAULT 'pendiente',
    CONSTRAINT fk_articulos_clientes
        FOREIGN KEY (id_cliente)
        REFERENCES Clientes(id_cliente)
        ON DELETE CASCADE
) ENGINE=InnoDB;

CREATE TABLE Citas (
    id_cita    INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT NOT NULL,
    fecha_hora DATETIME NOT NULL,
    CONSTRAINT fk_citas_clientes
        FOREIGN KEY (id_cliente)
        REFERENCES Clientes(id_cliente)
        ON DELETE CASCADE
) ENGINE=InnoDB;

CREATE TABLE Pagos (
    id_pago    INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT NOT NULL,
    monto      DECIMAL(10,2) NOT NULL,
    fecha_pago DATETIME NOT NULL,
    CONSTRAINT fk_pagos_clientes
        FOREIGN KEY (id_cliente)
        REFERENCES Clientes(id_cliente)
        ON DELETE CASCADE
) ENGINE=InnoDB;

-- =========================================
-- 3. DML - INSERTAR DATOS DE EJEMPLO
-- =========================================

-- Insertar clientes
INSERT INTO Clientes (nombre, telefono, direccion) VALUES
('Juan Pérez',      '555-1111', 'Calle 123 #10-20'),
('Laura Gómez',     '555-2222', 'Av. Central 456'),
('Carlos Sánchez',  '555-3333', 'Pasaje Norte 789'),
('Ana Martínez',    '555-4444', 'Calle Sur 321');

-- Insertar artículos por cliente
INSERT INTO Articulos (id_cliente, tipo_articulo, estado) VALUES
(1, 'Notebook Dell',        'pendiente'),
(1, 'Impresora HP',         'pendiente'),
(2, 'Celular Samsung',      'pendiente'),
(2, 'Tablet iPad',          'pendiente'),
(3, 'PC Escritorio Lenovo', 'pendiente'),
(4, 'Monitor LG 24"',       'pendiente');

-- Insertar citas
INSERT INTO Citas (id_cliente, fecha_hora) VALUES
(1, '2025-03-10 10:00:00'),
(1, '2025-03-15 15:00:00'),
(2, '2025-03-11 09:30:00'),
(3, '2025-03-12 16:00:00'),
(4, '2025-03-13 14:00:00');

-- Insertar pagos
INSERT INTO Pagos (id_cliente, monto, fecha_pago) VALUES
(1, 25.00, '2025-03-10 12:00:00'),
(1, 15.00, '2025-03-16 13:00:00'),
(2, 30.00, '2025-03-11 11:00:00'),
(3, 40.00, '2025-03-12 17:00:00');

-- =========================================
-- 4. DML - ACTUALIZACIONES (UPDATE)
-- =========================================

-- Actualizar cita por conflicto de horario (id_cita=2)
UPDATE Citas
SET fecha_hora = '2025-03-16 11:00:00'
WHERE id_cita = 2;

-- Actualizar estado de artículo (de pendiente a reciclado)
UPDATE Articulos
SET estado = 'reciclado'
WHERE id_articulo = 1;

-- =========================================
-- 5. DML - ELIMINACIONES (DELETE)
-- =========================================

-- Eliminar artículo registrado por error (id_articulo=6)
DELETE FROM Articulos
WHERE id_articulo = 6;

-- Eliminar cita cancelada (id_cita=5)
DELETE FROM Citas
WHERE id_cita = 5;

-- =========================================
-- 6. TRANSACCIONES - DEMOSTRACIÓN ACID
-- =========================================

-- Configurar manejo manual de transacciones
SET autocommit = 0;

-- TRANSACCIÓN 1: PROCESO COMPLETO EXITOSO
START TRANSACTION;

INSERT INTO Clientes (nombre, telefono, direccion)
VALUES ('María López', '555-4444', 'Calle Verde 101');

-- Nuevo cliente tiene id_cliente=5 (AUTO_INCREMENT)
INSERT INTO Articulos (id_cliente, tipo_articulo, estado)
VALUES (5, 'Televisor Sony 32"', 'pendiente');

INSERT INTO Citas (id_cliente, fecha_hora)
VALUES (5, '2025-03-18 09:00:00');

INSERT INTO Pagos (id_cliente, monto, fecha_pago)
VALUES (5, 35.00, '2025-03-18 10:00:00');

COMMIT;

-- TRANSACCIÓN 2: EJEMPLO CON ERROR (ROLLBACK)
START TRANSACTION;

INSERT INTO Clientes (nombre, telefono, direccion)
VALUES ('Pedro Error', '555-9999', 'Dirección inválida');

-- Intentar insertar artículo con id_cliente inexistente (provoca error FK)
INSERT INTO Articulos (id_cliente, tipo_articulo, estado)
VALUES (999, 'CPU Intel', 'pendiente'); -- ERROR: FK violation

-- ROLLBACK revierte TODAS las operaciones de esta transacción
ROLLBACK;

-- Restaurar autocommit
SET autocommit = 1;

-- =========================================
-- 7. CONSULTAS DE VERIFICACIÓN (BONUS)
-- =========================================

-- Verificar datos finales
SELECT 'CLIENTES' as Tabla;
SELECT * FROM Clientes;

SELECT 'ARTICULOS' as Tabla;
SELECT * FROM Articulos;

SELECT 'CITAS' as Tabla;
SELECT * FROM Citas;

SELECT 'PAGOS' as Tabla;
SELECT * FROM Pagos;

SELECT 
    c.nombre,
    COUNT(p.id_pago) as total_pagos,
    SUM(p.monto) as monto_total
FROM Clientes c
LEFT JOIN Pagos p ON c.id_cliente = p.id_cliente
GROUP BY c.id_cliente, c.nombre
ORDER BY monto_total DESC;

SELECT 
    c.nombre,
    a.tipo_articulo,
    a.estado,
    cit.fecha_hora
FROM Articulos a
JOIN Clientes c ON a.id_cliente = c.id_cliente
JOIN Citas cit ON a.id_cliente = cit.id_cliente
WHERE a.estado = 'pendiente'
ORDER BY cit.fecha_hora;
