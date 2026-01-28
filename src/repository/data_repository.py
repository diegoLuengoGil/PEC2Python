import json
from typing import Dict, Any, List
from src.database.db_manager import DBManager


class DataRepository:
    def __init__(self, db_manager: DBManager):
        self.db_manager = db_manager

    def export_all(self, file_path: str) -> bool:
        """Exporta tablas relevantes a un archivo JSON."""
        try:
            conn = self.db_manager.get_connection()
            cursor = conn.cursor()

            result: Dict[str, Any] = {}

            # Productos
            cursor.execute("SELECT id, nombre, descripcion, precio, stock, categoria FROM productos")
            filas = cursor.fetchall() 
            productos = []

            for row in filas:
                diccionario = {
                    "id": row[0],
                    "nombre": row[1],
                    "descripcion": row[2],
                    "precio": row[3],
                    "stock": row[4],
                    "categoria": row[5]
                }
                productos.append(diccionario)

            result["productos"] = productos

            # Clientes
            cursor.execute("SELECT id, nombre, email, saldo FROM clientes")
            filas = cursor.fetchall()
            clientes = []

            for row in filas:
                diccionario = {
                    "id": row[0],
                    "nombre": row[1],
                    "email": row[2],
                    "saldo": row[3]
                }
                clientes.append(diccionario)
            result["clientes"] = clientes

            # Ventas + items
            cursor.execute("SELECT id, total, estado FROM ventas")
            ventas_rows = cursor.fetchall()
            ventas = []

            for v in ventas_rows:
                id_venta_actual = v[0]
                
                cursor.execute("SELECT id, venta_id, producto_id, cantidad, subtotal FROM lineas_venta WHERE venta_id = ?", (id_venta_actual,))
                filas_items = cursor.fetchall()
                
                lista_items_objetos = []
                for row in filas_items:
                    item_diccionario = {
                        "id": row[0],
                        "venta_id": row[1],
                        "producto_id": row[2],
                        "cantidad": row[3],
                        "subtotal": row[4]
                    }
                    lista_items_objetos.append(item_diccionario)

                venta_diccionario = {
                    "id": v[0],
                    "total": v[1],
                    "estado": v[2],
                    "items": lista_items_objetos
                }
                
                ventas.append(venta_diccionario)

            result["ventas"] = ventas

            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(result, f, ensure_ascii=False, indent=2)

            return True
        except Exception as e:
            print(f"Error exporting to JSON: {e}")
            return False

    def import_all(self, file_path: str, overwrite: bool = False) -> bool:
        """Importa datos desde un JSON. Si overwrite=True, borra tablas antes de insertar. """
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)

            conn = self.db_manager.get_connection()
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
            except Exception as e:
                print(f"Error rolling back: {e}")
            return False
