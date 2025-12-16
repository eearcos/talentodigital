DROP DATABASE IF EXISTS libreria_db;
CREATE DATABASE libreria_db;
USE libreria_db;

CREATE TABLE Clientes (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    nombre_cliente VARCHAR(100) NOT NULL,
    correo_cliente VARCHAR(100) NOT NULL UNIQUE,
    telefono_cliente VARCHAR(15) NOT NULL CHECK (telefono_cliente REGEXP '^[0-9]{10}$'),
    direccion_cliente VARCHAR(255) NOT NULL
) ENGINE=InnoDB;

CREATE TABLE Libros (
    id_libro INT AUTO_INCREMENT PRIMARY KEY,
    titulo_libro VARCHAR(255) NOT NULL,
    autor_libro VARCHAR(100) NOT NULL,
    precio_libro DECIMAL(10,2) NOT NULL,
    cantidad_disponible INT NOT NULL CHECK (cantidad_disponible >= 0),
    categoria_libro VARCHAR(50) NOT NULL
) ENGINE=InnoDB;

CREATE TABLE Pedidos (
    id_pedido INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT NOT NULL,
    fecha_pedido DATE NOT NULL,
    total_pedido DECIMAL(10,2) NOT NULL,
    estado_pedido VARCHAR(50) NOT NULL,
    CONSTRAINT fk_pedidos_clientes
        FOREIGN KEY (id_cliente) REFERENCES Clientes(id_cliente)
        ON DELETE CASCADE
) ENGINE=InnoDB;

CREATE TABLE Detalles_Pedido (
    id_detalle INT AUTO_INCREMENT PRIMARY KEY,
    id_pedido INT NOT NULL,
    id_libro INT NOT NULL,
    cantidad_libro INT NOT NULL CHECK (cantidad_libro > 0),
    precio_libro DECIMAL(10,2) NOT NULL,
    CONSTRAINT fk_detalles_pedidos
        FOREIGN KEY (id_pedido) REFERENCES Pedidos(id_pedido)
        ON DELETE CASCADE,
    CONSTRAINT fk_detalles_libros
        FOREIGN KEY (id_libro) REFERENCES Libros(id_libro)
        ON DELETE RESTRICT
) ENGINE=InnoDB;

CREATE TABLE Pagos (
    id_pago INT AUTO_INCREMENT PRIMARY KEY,
    id_pedido INT NOT NULL,
    fecha_pago DATE NOT NULL,
    monto_pago DECIMAL(10,2) NOT NULL,
    metodo_pago VARCHAR(50) NOT NULL,
    CONSTRAINT fk_pagos_pedidos
        FOREIGN KEY (id_pedido) REFERENCES Pedidos(id_pedido)
        ON DELETE CASCADE
) ENGINE=InnoDB;

INSERT INTO Clientes (nombre_cliente, correo_cliente, telefono_cliente, direccion_cliente) VALUES
('Juan Pérez', 'juan@email.com', '5551234567', 'Calle 123 #45'),
('María Gómez', 'maria@email.com', '5552345678', 'Av. Central 678'),
('Carlos López', 'carlos@email.com', '5553456789', 'Pasaje Norte 12');

INSERT INTO Libros (titulo_libro, autor_libro, precio_libro, cantidad_disponible, categoria_libro) VALUES
('Cien Años de Soledad', 'Gabriel García Márquez', 25.99, 50, 'Novela'),
('1984', 'George Orwell', 19.99, 30, 'Distopía'),
('El Quijote', 'Miguel de Cervantes', 35.50, 20, 'Clásico');

INSERT INTO Pedidos (id_cliente, fecha_pedido, total_pedido, estado_pedido) VALUES
(1, '2025-03-10', 45.98, 'procesando'),
(2, '2025-03-11', 25.99, 'enviado'),
(1, '2025-03-12', 19.99, 'entregado');

INSERT INTO Detalles_Pedido (id_pedido, id_libro, cantidad_libro, precio_libro) VALUES
(1, 1, 1, 25.99),
(1, 2, 1, 19.99),
(2, 1, 1, 25.99),
(3, 2, 1, 19.99);

INSERT INTO Pagos (id_pedido, fecha_pago, monto_pago, metodo_pago) VALUES
(1, '2025-03-10', 45.98, 'tarjeta'),
(2, '2025-03-11', 25.99, 'transferencia');

ALTER TABLE Clientes 
MODIFY COLUMN telefono_cliente VARCHAR(20) NOT NULL;

ALTER TABLE Libros 
MODIFY COLUMN precio_libro DECIMAL(10,3) NOT NULL;

ALTER TABLE Detalles_Pedido 
MODIFY COLUMN precio_libro DECIMAL(10,3) NOT NULL;

ALTER TABLE Pagos 
ADD COLUMN fecha_confirmacion DATE NULL AFTER metodo_pago;

UPDATE Pagos SET fecha_confirmacion = fecha_pago WHERE id_pago IN (1,2);

DROP TABLE Pagos;

CREATE TABLE Pagos (
    id_pago INT AUTO_INCREMENT PRIMARY KEY,
    id_pedido INT NOT NULL,
    fecha_pago DATE NOT NULL,
    monto_pago DECIMAL(10,3) NOT NULL,
    metodo_pago VARCHAR(50) NOT NULL,
    fecha_confirmacion DATE NULL,
    CONSTRAINT fk_pagos_pedidos
        FOREIGN KEY (id_pedido) REFERENCES Pedidos(id_pedido)
        ON DELETE CASCADE
) ENGINE=InnoDB;

INSERT INTO Pagos (id_pedido, fecha_pago, monto_pago, metodo_pago) VALUES
(1, '2025-03-10', 45.980, 'tarjeta'),
(3, '2025-03-12', 19.990, 'efectivo');

SET FOREIGN_KEY_CHECKS = 0;
TRUNCATE TABLE Pedidos;
SET FOREIGN_KEY_CHECKS = 1;


SELECT '=== CLIENTES ===' as Tabla;
SELECT * FROM Clientes;

SELECT '=== LIBROS ===' as Tabla;
SELECT * FROM Libros;

SELECT '=== PEDIDOS (TRUNCADOS) ===' as Tabla;
SELECT * FROM Pedidos;

SELECT '=== DETALLES_PEDIDO ===' as Tabla;
SELECT * FROM Detalles_Pedido;

SELECT '=== PAGOS ===' as Tabla;
SELECT * FROM Pagos;

SELECT 
    l.titulo_libro,
    l.autor_libro,
    SUM(dp.cantidad_libro) as total_vendidos
FROM Libros l
JOIN Detalles_Pedido dp ON l.id_libro = dp.id_libro
GROUP BY l.id_libro, l.titulo_libro, l.autor_libro
ORDER BY total_vendidos DESC;

SELECT 
    c.nombre_cliente,
    COUNT(p.id_pedido) as total_pedidos
FROM Clientes c
LEFT JOIN Pedidos p ON c.id_cliente = p.id_cliente
GROUP BY c.id_cliente, c.nombre_cliente
ORDER BY total_pedidos DESC;
