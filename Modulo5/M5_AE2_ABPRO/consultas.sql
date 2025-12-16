SELECT DISTINCT c.nombre, c.telefono, c.email
FROM Clientes c
JOIN Alquileres a ON c.id_cliente = a.id_cliente
WHERE CURRENT_DATE() BETWEEN a.fecha_inicio AND a.fecha_fin;

SELECT DISTINCT v.modelo,v.marca,v.precio_dia
FROM Vehiculos v
JOIN Alquileres a ON v.id_vehiculo = a.id_vehiculo
WHERE a.fecha_inicio >= '2025-03-01'
AND a.fecha_inicio <  '2025-04-01';

SELECT c.nombre, a.id_alquiler,
(DATEDIFF(a.fecha_fin, a.fecha_inicio) + 1) * v.precio_dia AS precio_total
FROM Clientes c
JOIN Alquileres a ON c.id_cliente = a.id_cliente
JOIN Vehiculos v  ON a.id_vehiculo = v.id_vehiculo;

SELECT
    c.nombre,
    c.email
FROM Clientes c
LEFT JOIN Alquileres a ON c.id_cliente = a.id_cliente
LEFT JOIN Pagos p      ON a.id_alquiler = p.id_alquiler
WHERE p.id_pago IS NULL;

SELECT c.nombre,
    AVG(p.monto) AS promedio_pago
FROM Clientes c
JOIN Alquileres a ON c.id_cliente = a.id_cliente
JOIN Pagos p      ON a.id_alquiler = p.id_alquiler
GROUP BY c.id_cliente, c.nombre;

SELECT v.modelo, v.marca, v.precio_dia
FROM Vehiculos v
WHERE v.id_vehiculo NOT IN (
    SELECT a.id_vehiculo
    FROM Alquileres a
    WHERE '2025-03-18' BETWEEN a.fecha_inicio AND a.fecha_fin
);

SELECT v.marca, v.modelo,
    COUNT(*) AS cantidad_alquileres
FROM Vehiculos v
JOIN Alquileres a ON v.id_vehiculo = a.id_vehiculo
WHERE a.fecha_inicio >= '2025-03-01'
AND a.fecha_inicio <  '2025-04-01'
GROUP BY v.id_vehiculo, v.marca, v.modelo
HAVING COUNT(*) > 1;

SELECT c.nombre,
    SUM(p.monto) AS total_pagado
FROM Clientes c
JOIN Alquileres a ON c.id_cliente = a.id_cliente
JOIN Pagos p      ON a.id_alquiler = p.id_alquiler
GROUP BY c.id_cliente, c.nombre;

SELECT c.nombre, a.fecha_inicio, a.fecha_fin
FROM Clientes c
JOIN Alquileres a ON c.id_cliente = a.id_cliente
WHERE a.id_vehiculo = 3;

SELECT c.nombre,
    SUM(DATEDIFF(a.fecha_fin, a.fecha_inicio) + 1) AS total_dias_alquilados
FROM Clientes c
JOIN Alquileres a ON c.id_cliente = a.id_cliente
GROUP BY c.id_cliente, c.nombre
ORDER BY total_dias_alquilados DESC;
