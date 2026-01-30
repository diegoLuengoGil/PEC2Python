from repository.cliente_repository import ClienteRepository
from models.cliente import Cliente
from typing import Optional

class ClienteService:
    def __init__(self, repositorio: ClienteRepository):
        self.repositorio = repositorio
    
    def agregar_cliente(self, cliente: Cliente) -> bool:
        """Agrega un nuevo cliente."""
        resultado = False
        if cliente.saldo < 0:
            print("El saldo no puede ser negativo.")
        else:
            # Aquí se podrían añadir más validaciones, como comprobar formato de email
            resultado = self.repositorio.agregar_cliente(cliente)
        return resultado
    
    def eliminar_cliente(self, id_cliente: int) -> bool:
        """Elimina un cliente por ID."""
        return self.repositorio.eliminar_cliente(id_cliente)
    
    def modificar_cliente(self, cliente: Cliente) -> bool:
        """Modifica un cliente existente."""
        resultado = False
        if cliente.saldo < 0:
            print("El saldo no puede ser negativo.")
        else:
            resultado = self.repositorio.modificar_cliente(cliente)
        return resultado

    def listar_clientes(self) -> list[Cliente]:
        """Lista todos los clientes."""
        return self.repositorio.listar_clientes()

    def obtener_cliente(self, id_cliente: int) -> Optional[Cliente]:
        """Obtiene un cliente por ID."""
        return self.repositorio.obtener_cliente_por_id(id_cliente)
