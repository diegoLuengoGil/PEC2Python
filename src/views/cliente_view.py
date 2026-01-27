from src.utils.utils import Utils
from src.models.cliente import Cliente
from typing import List

class ClienteView:
    def mostrar_menu(self) -> int:
        print("\n--- Menú de Gestión de Clientes ---")
        print("1. Añadir cliente")
        print("2. Modificar cliente")
        print("3. Eliminar cliente")
        print("4. Mostrar clientes")
        print("0. Volver al menú principal")
        opcion = Utils.get_int("Seleccione una opción: ")
        return opcion

    def solicitar_datos_cliente(self) -> dict:
        """Solicita los datos de un nuevo cliente."""
        print("\nIngrese los datos del cliente:")
        nombre = Utils.get_non_empty_str("Nombre: ")
        email = Utils.get_non_empty_str("Email: ")
        saldo = Utils.get_float("Saldo inicial: ")
        datos = {
            "nombre": nombre,
            "email": email,
            "saldo": saldo
        }
        return datos

    def solicitar_id_cliente(self) -> int:
        id_cliente = Utils.get_int("Ingrese el ID del cliente: ")
        return id_cliente

    def mostrar_mensaje(self, mensaje: str):
        print(f"\n{mensaje}")
        
    def mostrar_cliente(self, cliente: Cliente):
        print(f"\nID: {cliente.id}")
        print(f"Nombre: {cliente.nombre}")
        print(f"Email: {cliente.email}")
        print(f"Saldo: {cliente.saldo:.2f}")


    def mostrar_lista_clientes(self, clientes: List[Cliente]):
        if not clientes:
            print("\nNo hay clientes registrados.")
        else:
            print("\n--- Lista de Clientes ---")
            print(f"{'ID':<5} {'Nombre':<25} {'Email':<30} {'Saldo':<10}")
            print("-" * 75)
            for c in clientes:
                print(f"{c.id:<5} {c.nombre[:25]:<25} {c.email[:30]:<30} {c.saldo:<10.2f}")
