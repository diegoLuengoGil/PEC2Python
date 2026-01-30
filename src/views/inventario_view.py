from utils.utils import Utils
from models.producto import Producto

class InventarioView:
    def mostrar_menu(self) -> int:
        print("\n--- Menú de Inventario ---")
        print("1. Añadir artículo")
        print("2. Modificar artículo")
        print("3. Eliminar artículo")
        print("4. Mostrar inventario")
        print("0. Volver al menú principal")
        opcion = Utils.get_int("Seleccione una opción: ")
        return opcion

    def solicitar_datos_producto(self) -> dict:
        """Solicita los datos de un nuevo producto al usuario."""
        print("\nIngrese los datos del producto:")
        nombre = Utils.get_non_empty_str("Nombre: ")
        descripcion = input("Descripción: ").strip()
        precio = Utils.get_float("Precio: ")
        stock = Utils.get_int("Stock: ")
        categoria = Utils.get_non_empty_str("Categoría: ")
        datos = {
            "nombre": nombre,
            "descripcion": descripcion,
            "precio": precio,
            "stock": stock,
            "categoria": categoria
        }
        return datos

    def solicitar_id_producto(self) -> int:
        id_producto = Utils.get_int("Ingrese el ID del producto: ")
        return id_producto

    def mostrar_mensaje(self, mensaje: str):
        print(f"\n{mensaje}")
        
    def mostrar_producto(self, producto: Producto):
        print(f"\nID: {producto.id}")
        print(f"Nombre: {producto.nombre}")
        print(f"Descripción: {producto.descripcion}")
        print(f"Precio: {producto.precio:.2f}")
        print(f"Stock: {producto.stock}")
        print(f"Categoría: {producto.categoria}")

    def mostrar_lista_productos(self, productos: list[Producto]):
        if not productos:
            print("\nNo hay productos en el inventario.")
        else:
            print("\n--- Lista de Productos ---")
            print(f"{'ID':<5} {'Nombre':<20} {'Precio':<10} {'Stock':<10} {'Categoría':<15}")
            print("-" * 65)
            for p in productos:
                print(f"{p.id:<5} {p.nombre[:20]:<20} {p.precio:<10.2f} {p.stock:<10} {p.categoria[:15]:<15}")