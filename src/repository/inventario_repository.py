from src.database.db_manager import DBManager
from src.models.producto import Producto
from typing import List, Optional

class InventarioRepository:
    """Gestión de productos (CRUD)."""

    def __init__(self, db_manager: DBManager):
        self.db_manager = db_manager

    def agregar_producto(self, producto: Producto) -> bool:
        """Inserta un nuevo producto en la base de datos."""
        query = "INSERT INTO productos (nombre, descripcion, precio, stock, categoria) VALUES (?, ?, ?, ?, ?)"
        conn = self.db_manager.get_connection()
        exito = False
        try:
            cursor = conn.cursor()
            cursor.execute(query, (producto.nombre, producto.descripcion, producto.precio, producto.stock, producto.categoria))
            conn.commit()
            exito = True
        except Exception as e:
            print(f"Error al agregar producto: {e}")
            exito = False
        return exito

    def eliminar_producto(self, id_producto: int) -> bool:
        """Elimina un producto por su ID."""
        query = "DELETE FROM productos WHERE id = ?"
        conn = self.db_manager.get_connection()
        exito = False
        try:
            cursor = conn.cursor()
            cursor.execute(query, (id_producto,))
            conn.commit()
            exito = cursor.rowcount > 0
        except Exception as e:
            print(f"Error al eliminar producto: {e}")
            exito = False
        return exito

    def modificar_producto(self, producto: Producto) -> bool:
        """Modifica un producto existente."""
        query = """
            UPDATE productos 
            SET nombre = ?, descripcion = ?, precio = ?, stock = ?, categoria = ?
            WHERE id = ?
        """
        conn = self.db_manager.get_connection()
        exito = False
        try:
            cursor = conn.cursor()
            cursor.execute(query, (producto.nombre, producto.descripcion, producto.precio, producto.stock, producto.categoria, producto.id))
            conn.commit()
            exito = cursor.rowcount > 0
        except Exception as e:
            print(f"Error al modificar producto: {e}")
            exito = False
        return exito

    def listar_productos(self) -> List[Producto]:
        """Devuelve una lista con todos los productos."""
        query = "SELECT id, nombre, descripcion, precio, stock, categoria FROM productos"
        conn = self.db_manager.get_connection()
        productos = []
        try:
            cursor = conn.cursor()
            cursor.execute(query)
            rows = cursor.fetchall()
            for row in rows:
                productos.append(Producto(
                    id=row[0],
                    nombre=row[1],
                    descripcion=row[2],
                    precio=row[3],
                    stock=row[4],
                    categoria=row[5]
                ))
        except Exception as e:
            print(f"Error al listar productos: {e}")
        return productos

    def obtener_producto_por_id(self, id_producto: int) -> Optional[Producto]:
        """Obtiene un producto por su ID."""
        query = "SELECT id, nombre, descripcion, precio, stock, categoria FROM productos WHERE id = ?"
        conn = self.db_manager.get_connection()
        producto = None
        try:
            cursor = conn.cursor()
            cursor.execute(query, (id_producto,))
            row = cursor.fetchone()
            if row:
                producto = Producto(
                    id=row[0],
                    nombre=row[1],
                    descripcion=row[2],
                    precio=row[3],
                    stock=row[4],
                    categoria=row[5]
                )
        except Exception as e:
            print(f"Error al obtener producto: {e}")
        return producto