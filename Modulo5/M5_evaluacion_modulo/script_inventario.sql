CREATE TABLE Proveedores (
    id_proveedor INT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    direccion VARCHAR(150),
    telefono VARCHAR(20),
    email VARCHAR(100)
);

CREATE TABLE Productos (
    id_producto INT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT,
    precio DECIMAL(10, 2) NOT NULL CHECK (precio > 0),
    cantidad_stock INT NOT NULL CHECK (cantidad_stock >= 0)
);

CREATE TABLE Transacciones (
    id_transaccion INT PRIMARY KEY,
    tipo VARCHAR(10) NOT NULL CHECK (tipo IN ('COMPRA', 'VENTA')),
    fecha DATE NOT NULL,
    cantidad INT NOT NULL CHECK (cantidad > 0),
    id_producto INT,
    id_proveedor INT,
    FOREIGN KEY (id_producto) REFERENCES Productos(id_producto),
    FOREIGN KEY (id_proveedor) REFERENCES Proveedores(id_proveedor)
);

INSERT INTO Proveedores VALUES 
(1, 'TecnoGlobal S.A.', 'Av. Siempre Viva 123', '555-0101', 'contacto@tecnoglobal.com'),
(2, 'Distribuidora Norte', 'Calle Falsa 456', '555-0202', 'ventas@distnorte.com');

INSERT INTO Productos VALUES 
(101, 'Laptop Gamer', 'Laptop 16GB RAM', 1200.00, 10),
(102, 'Mouse Inalámbrico', 'Mouse óptico', 25.50, 50),
(103, 'Monitor 24"', 'Monitor LED Full HD', 180.00, 20);

INSERT INTO Transacciones VALUES 
(1, 'COMPRA', '2023-10-01', 10, 101, 1), 
(2, 'VENTA', '2023-10-05', 2, 101, 1),   
(3, 'VENTA', '2023-10-06', 5, 102, 2);   

BEGIN TRANSACTION;

INSERT INTO Transacciones (id_transaccion, tipo, fecha, cantidad, id_producto, id_proveedor)
VALUES (4, 'VENTA', '2023-10-27', 1, 103, 2);

UPDATE Productos 
SET cantidad_stock = cantidad_stock - 1 
WHERE id_producto = 103;

COMMIT;

SELECT * FROM Productos WHERE cantidad_stock > 0;

SELECT id_producto, SUM(cantidad) as total_vendidos
FROM Transacciones
WHERE tipo = 'VENTA'
GROUP BY id_producto;

SELECT 
    T.fecha,
    P.nombre AS Producto,
    Pr.nombre AS Proveedor_Relacionado,
    T.cantidad,
    (T.cantidad * P.precio) AS total_dinero
FROM Transacciones T
INNER JOIN Productos P ON T.id_producto = P.id_producto
LEFT JOIN Proveedores Pr ON T.id_proveedor = Pr.id_proveedor
WHERE T.tipo = 'VENTA';

SELECT nombre 
FROM Productos 
WHERE id_producto NOT IN (
    SELECT DISTINCT id_producto 
    FROM Transacciones 
    WHERE tipo = 'VENTA'
);