from src.database.db_manager import DBManager
from src.models.venta import Venta
from src.models.item_venta import ItemVenta
from typing import List, Optional

class VentaRepository:
    def __init__(self, db_manager: DBManager):
        self.db_manager = db_manager

    def crear_venta(self, venta: Venta) -> bool:
        """Crea una nueva venta y sus líneas de detalle en una transacción."""
        conn = self.db_manager.get_connection()
        try:
            cursor = conn.cursor()
            # 1. Insertar venta
            query_venta = "INSERT INTO ventas (total, estado) VALUES (?, ?)"
            cursor.execute(query_venta, (venta.total, venta.estado))
            venta_id = cursor.lastrowid
            
            # 2. Insertar items
            query_item = "INSERT INTO lineas_venta (venta_id, producto_id, cantidad, subtotal) VALUES (?, ?, ?, ?)"
            for item in venta.items:
                cursor.execute(query_item, (venta_id, item.producto_id, item.cantidad, item.subtotal))
                item.venta_id = venta_id
            
            conn.commit()
            return True
        except Exception as e:
            conn.rollback()
            print(f"Error al crear venta: {e}")
            return False

    def listar_ventas(self) -> List[Venta]:
        """Lista todas las ventas (sin el detalle de items por eficiencia en listado simple)."""
        query = "SELECT id, total, estado FROM ventas"
        conn = self.db_manager.get_connection()
        ventas = []
        try:
            cursor = conn.cursor()
            cursor.execute(query)
            rows = cursor.fetchall()
            for row in rows:
                ventas.append(Venta(
                    id=row[0],
                    total=row[1],
                    estado=row[2]
                ))
        except Exception as e:
            print(f"Error al listar ventas: {e}")
        return ventas

    def obtener_venta_por_id(self, id_venta: int) -> Optional[Venta]:
        """Obtiene una venta con todos sus detalles (items)."""
        conn = self.db_manager.get_connection()
        try:
            cursor = conn.cursor()
            # Obtener cabecera
            cursor.execute("SELECT id, total, estado FROM ventas WHERE id = ?", (id_venta,))
            row = cursor.fetchone()
            if not row:
                return None
            
            venta = Venta(id=row[0], total=row[1], estado=row[2])
            
            # Obtener items
            cursor.execute("SELECT id, venta_id, producto_id, cantidad, subtotal FROM lineas_venta WHERE venta_id = ?", (id_venta,))
            rows_items = cursor.fetchall()
            items = []
            for r in rows_items:
                items.append(ItemVenta(
                    id=r[0],
                    venta_id=r[1],
                    producto_id=r[2],
                    cantidad=r[3],
                    subtotal=r[4]
                ))
            venta.items = items
            return venta
        except Exception as e:
            print(f"Error al obtener venta: {e}")
            return None
