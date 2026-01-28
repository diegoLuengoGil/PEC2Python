import json
from typing import Dict, Any
from src.database.db_manager import DBManager


def export_to_json(db_manager: DBManager, file_path: str) -> bool:
    """Exporta tablas relevantes a un archivo JSON.

    Formato simple: {"productos": [...], "clientes": [...], "ventas": [{... , "items": [...]}, ...]}
    """
    try:
        conn = db_manager.get_connection()
        cursor = conn.cursor()

        result: Dict[str, Any] = {}

        # Productos
        cursor.execute("SELECT id, nombre, descripcion, precio, stock, categoria FROM productos")
        productos = [
            {
                "id": row[0],
                "nombre": row[1],
                "descripcion": row[2],
                "precio": row[3],
                "stock": row[4],
                "categoria": row[5],
            }
            for row in cursor.fetchall()
        ]
        result["productos"] = productos

        # Clientes
        cursor.execute("SELECT id, nombre, email, saldo FROM clientes")
        clientes = [
            {"id": r[0], "nombre": r[1], "email": r[2], "saldo": r[3]}
            for r in cursor.fetchall()
        ]
        result["clientes"] = clientes

        # Ventas + items
        cursor.execute("SELECT id, total, estado FROM ventas")
        ventas_rows = cursor.fetchall()
        ventas = []
        for v in ventas_rows:
            venta_id = v[0]
            cursor.execute("SELECT id, venta_id, producto_id, cantidad, subtotal FROM lineas_venta WHERE venta_id = ?", (venta_id,))
            items = [
                {"id": it[0], "venta_id": it[1], "producto_id": it[2], "cantidad": it[3], "subtotal": it[4]}
                for it in cursor.fetchall()
            ]
            ventas.append({"id": v[0], "total": v[1], "estado": v[2], "items": items})
        result["ventas"] = ventas

        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False, indent=2)

        return True
    except Exception as e:
        print(f"Error exporting to JSON: {e}")
        return False


def import_from_json(db_manager: DBManager, file_path: str, overwrite: bool = False) -> bool:
    """Importa datos desde un JSON. Si overwrite=True, borra tablas antes de insertar.

    Nota: Esta función asume las mismas columnas que el esquema y hace inserciones básicas.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        conn = db_manager.get_connection()
        cursor = conn.cursor()

        if overwrite:
            cursor.execute("DELETE FROM lineas_venta")
            cursor.execute("DELETE FROM ventas")
            cursor.execute("DELETE FROM productos")
            cursor.execute("DELETE FROM clientes")
            conn.commit()

        # Insert productos
        for p in data.get('productos', []):
            cursor.execute(
                "INSERT INTO productos (id, nombre, descripcion, precio, stock, categoria) VALUES (?, ?, ?, ?, ?, ?)",
                (p.get('id'), p.get('nombre'), p.get('descripcion'), p.get('precio'), p.get('stock'), p.get('categoria'))
            )

        # Insert clientes
        for c in data.get('clientes', []):
            cursor.execute(
                "INSERT INTO clientes (id, nombre, email, saldo) VALUES (?, ?, ?, ?)",
                (c.get('id'), c.get('nombre'), c.get('email'), c.get('saldo'))
            )

        # Insert ventas and items
        for v in data.get('ventas', []):
            cursor.execute("INSERT INTO ventas (id, total, estado) VALUES (?, ?, ?)", (v.get('id'), v.get('total'), v.get('estado')))
            for it in v.get('items', []):
                cursor.execute(
                    "INSERT INTO lineas_venta (id, venta_id, producto_id, cantidad, subtotal) VALUES (?, ?, ?, ?, ?)",
                    (it.get('id'), it.get('venta_id'), it.get('producto_id'), it.get('cantidad'), it.get('subtotal'))
                )

        conn.commit()
        return True
    except FileNotFoundError:
        print("Error: JSON file not found.")
        return False
    except Exception as e:
        print(f"Error importing from JSON: {e}")
        try:
            conn.rollback()
        except Exception:
            pass
        return False
