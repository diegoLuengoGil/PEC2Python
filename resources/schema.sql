-- Script for creating the database schema
-- Ensures tables are created if they do not exist (idempotent)

BEGIN TRANSACTION;

-- Table: productos
-- Stores inventory items
CREATE TABLE IF NOT EXISTS productos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    descripcion TEXT,
    precio REAL NOT NULL CHECK(precio >= 0),
    stock INTEGER NOT NULL DEFAULT 0 CHECK(stock >= 0),
    categoria TEXT
);

-- Table: ventas
-- Stores sales transactions header
CREATE TABLE IF NOT EXISTS ventas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    total REAL DEFAULT 0.0,
    estado TEXT DEFAULT 'COMPLETADA' -- COMPLETADA, CANCELADA
);

-- Table: lineas_venta
-- Stores individual items belonging to a sale
CREATE TABLE IF NOT EXISTS lineas_venta (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    venta_id INTEGER NOT NULL,
    producto_id INTEGER NOT NULL,
    cantidad INTEGER NOT NULL CHECK(cantidad > 0),
    subtotal REAL NOT NULL CHECK(subtotal >= 0),
    FOREIGN KEY (venta_id) REFERENCES ventas(id) ON DELETE CASCADE,
    FOREIGN KEY (producto_id) REFERENCES productos(id)
);

-- Table: clientes
-- Stores customer information
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    saldo REAL DEFAULT 0.0 CHECK(saldo >= 0)
);

COMMIT;
