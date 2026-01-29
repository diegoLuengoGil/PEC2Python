from src.utils.utils import Utils
from src.models.venta import Venta
from typing import List, Dict

class VentaView:
    def mostrar_menu(self) -> int:
        print("\n--- Menú de Gestión de Ventas ---")
        print("1. Nueva venta")
        print("2. Mostrar historial de ventas")
        print("3. Detalle de venta")
        print("0. Volver al menú principal")
        opcion = Utils.get_int("Seleccione una opción: ")
        return opcion

    def solicitar_cliente_id(self) -> int:
        """Solicita el ID del cliente para la venta."""
        return Utils.get_int("Ingrese el ID del Cliente: ")

    def solicitar_items_venta(self) -> List[Dict[str, int]]:
        """Solicita al usuario los productos y cantidades para una venta."""
        items = []
        continuar = True
        print("\n--- Añadir Productos (Ingrese 0 en ID para finalizar) ---")
        while continuar:
            producto_id = Utils.get_int("ID del Producto: ")
            if producto_id == 0:
                continuar = False
            else:
                cantidad = Utils.get_int("Cantidad: ")
                if cantidad <= 0:
                    print("La cantidad debe ser mayor a 0.")
                else:
                    items.append({"producto_id": producto_id, "cantidad": cantidad})
                    
                    if not Utils.confirmar_accion("¿Añadir otro producto?"):
                        continuar = False
        return items

    def mostrar_mensaje(self, mensaje: str):
        print(f"\n{mensaje}")
        
    def mostrar_detalle_venta(self, venta: Venta):
        print(f"\n--- Detalle de Venta ID: {venta.id} ---")
        print(f"Cliente ID: {venta.cliente_id}")
        print(f"Estado: {venta.estado}")
        print(f"Total: {venta.total:.2f}")
        print("Items:")
        print(f"{'Producto ID':<12} {'Cant':<5} {'Subtotal':<10}")
        print("-" * 30)
        for item in venta.items:
            print(f"{item.producto_id:<12} {item.cantidad:<5} {item.subtotal:<10.2f}")

    def mostrar_lista_ventas(self, ventas: List[Venta]):
        if not ventas:
            print("\nNo hay ventas registradas.")
        else:
            print("\n--- Historial de Ventas ---")
            print(f"{'ID':<5} {'Total':<10} {'Estado':<15} {'Cliente ID':<10}")
            print("-" * 45)
            for v in ventas:
                print(f"{v.id:<5} {v.total:<10.2f} {v.estado:<15} {v.cliente_id:<10}")
        
    def solicitar_id_venta(self) -> int:
        id_venta = Utils.get_int("Ingrese el ID de la venta: ")
        return id_venta
