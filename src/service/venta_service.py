from src.repository.venta_repository import VentaRepository
from src.repository.inventario_repository import InventarioRepository
from src.models.venta import Venta
from src.models.item_venta import ItemVenta
from typing import List, Dict, Optional

class VentaService:
    def __init__(self, venta_repository: VentaRepository, inventario_repository: InventarioRepository):
        self.venta_repository = venta_repository
        self.inventario_repository = inventario_repository

    def crear_venta(self, items_solicitados: List[Dict[str, int]]) -> bool:
        """
        Crea una venta verificando stock y calculando totales.
        items_solicitados: lista de diccionarios {'producto_id': int, 'cantidad': int}
        """
        resultado = False
        if not items_solicitados:
            print("No se han seleccionado productos.")
        else:
            items_venta = []
            total_venta = 0.0
            error_validacion = False
            
            # 1. Validar stock y construir items
            productos_a_actualizar = []

            for req in items_solicitados:
                # Usamos un flag para continuar solo si no hubo error
                if not error_validacion:
                    prod_id = req['producto_id']
                    cantidad = req['cantidad']
                    
                    producto = self.inventario_repository.obtener_producto_por_id(prod_id)
                    if not producto:
                        print(f"Producto ID {prod_id} no encontrado.")
                        error_validacion = True
                    else:
                        if producto.stock < cantidad:
                            print(f"Stock insuficiente para '{producto.nombre}'. Disponible: {producto.stock}, Solicitado: {cantidad}")
                            error_validacion = True
                        else:
                            subtotal = producto.precio * cantidad
                            items_venta.append(ItemVenta(
                                id=0,
                                venta_id=0, # Se asignará al guardar
                                producto_id=prod_id,
                                cantidad=cantidad,
                                subtotal=subtotal
                            ))
                            total_venta += subtotal
                            
                            # Preparamos el producto con el nuevo stock para actualizarlo después
                            producto.stock -= cantidad
                            productos_a_actualizar.append(producto)

            if not error_validacion:
                # 2. Guardar venta
                venta = Venta(id=0, total=total_venta, estado="COMPLETADA", items=items_venta)
                if self.venta_repository.crear_venta(venta):
                    # 3. Actualizar stock
                    exito_stock = True
                    for prod in productos_a_actualizar:
                        if not self.inventario_repository.modificar_producto(prod):
                            print(f"Error al actualizar stock del producto {prod.nombre} (ID: {prod.id})")
                            exito_stock = False
                    
                    if exito_stock:
                        print(f"Venta registrada con éxito. Total: {total_venta:.2f}")
                        resultado = True
                    else:
                        print("Venta registrada pero hubo errores actualizando el stock.")
                        resultado = True # La venta se hizo aunque con warnings
                else:
                    print("Error al guardar la venta.")
                    resultado = False
            else:
                resultado = False
                
        return resultado

    def listar_ventas(self) -> List[Venta]:
        return self.venta_repository.listar_ventas()
    
    def obtener_venta(self, id_venta: int) -> Optional[Venta]:
        return self.venta_repository.obtener_venta_por_id(id_venta)
