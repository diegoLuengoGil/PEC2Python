-- Script for creating the database schema
-- Ensures tables are created if they do not exist (idempotent)

BEGIN TRANSACTION;

-- Table: products
-- Stores inventory items
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    price REAL NOT NULL CHECK(price >= 0),
    stock INTEGER NOT NULL DEFAULT 0 CHECK(stock >= 0),
    category TEXT
);

-- Table: sales
-- Stores sales transactions header
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sale_date TEXT NOT NULL DEFAULT (datetime('now', 'localtime')),
    total_amount REAL DEFAULT 0.0,
    status TEXT DEFAULT 'COMPLETED' -- COMPLETED, CANCELLED
);

-- Table: sale_items
-- Stores individual items belonging to a sale
CREATE TABLE IF NOT EXISTS sale_items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sale_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL CHECK(quantity > 0),
    subtotal REAL NOT NULL CHECK(subtotal >= 0),
    FOREIGN KEY (sale_id) REFERENCES sales(id) ON DELETE CASCADE,
    FOREIGN KEY (product_id) REFERENCES products(id)
);

COMMIT;
