
CREATE DATABASE IF NOT EXISTS tienda;
USE tienda;

CREATE TABLE clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre    VARCHAR(100) NOT NULL,
    direccion VARCHAR(200),
    telefono  VARCHAR(50)
) ENGINE=InnoDB;

CREATE TABLE pedidos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cliente_id INT NOT NULL,
    fecha DATE NOT NULL,
    total DECIMAL(10,2) NOT NULL,
    CONSTRAINT fk_pedidos_clientes
        FOREIGN KEY (cliente_id)
        REFERENCES clientes(id)
        ON DELETE CASCADE
) ENGINE=InnoDB;

INSERT INTO clientes (nombre, direccion, telefono) VALUES
('Juan Pérez',      'Calle 123',    '555-1111'),
('Laura Gómez',     'Av. Central',  '555-2222'),
('Carlos Sánchez',  'Pasaje Norte', '555-3333'),
('Ana Rodríguez',   'Calle Sur',    '555-4444'),
('Miguel Torres',   'Camino Real',  '555-5555');


INSERT INTO pedidos (cliente_id, fecha, total) VALUES
(1, '2025-03-01', 100.00),
(1, '2025-03-05',  50.00),
(2, '2025-03-02', 200.00),
(2, '2025-03-10',  80.00),
(3, '2025-03-03', 150.00),
(3, '2025-03-15',  60.00),
(4, '2025-03-04', 120.00),
(4, '2025-03-20',  90.00),
(5, '2025-03-06', 300.00),
(5, '2025-03-22', 110.00);


SELECT
    c.id        AS cliente_id,
    c.nombre    AS nombre_cliente,
    p.id        AS pedido_id,
    p.fecha,
    p.total
FROM clientes c
LEFT JOIN pedidos p ON c.id = p.cliente_id
ORDER BY c.id, p.fecha;

-- 6. Proyectar todos los pedidos de un cliente específico (ejemplo: id = 3)

SELECT
    p.id,
    p.fecha,
    p.total
FROM pedidos p
WHERE p.cliente_id = 3
ORDER BY p.fecha;

-- 7. Calcular el total de todos los pedidos para cada cliente

SELECT
    c.id,
    c.nombre,
    SUM(p.total) AS total_pedidos
FROM clientes c
JOIN pedidos p ON c.id = p.cliente_id
GROUP BY c.id, c.nombre
ORDER BY total_pedidos DESC;


UPDATE clientes
SET direccion = 'Nueva Dirección 456'
WHERE id = 2;


DELETE FROM clientes
WHERE id = 5;


SELECT
    c.id,
    c.nombre,
    COUNT(p.id) AS cantidad_pedidos
FROM clientes c
JOIN pedidos p ON c.id = p.cliente_id
GROUP BY c.id, c.nombre
ORDER BY cantidad_pedidos DESC
LIMIT 3;
