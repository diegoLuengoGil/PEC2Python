from src.database.db_manager import DBManager
from src.models.cliente import Cliente
from typing import List, Optional

class ClienteRepository:
    """Repositorio para gestionar operaciones relacionadas con clientes."""
    def __init__(self, db_manager: DBManager):
        self.db_manager = db_manager

    def agregar_cliente(self, cliente: Cliente) -> bool:
        """Inserta un nuevo cliente en la base de datos."""
        query = "INSERT INTO clientes (nombre, email, saldo) VALUES (?, ?, ?)"
        conn = self.db_manager.get_connection()
        exito = False
        try:
            cursor = conn.cursor()
            cursor.execute(query, (cliente.nombre, cliente.email, cliente.saldo))
            conn.commit()
            exito = True
        except Exception as e:
            print(f"Error al agregar cliente: {e}")
            exito = False
        return exito

    def eliminar_cliente(self, id_cliente: int) -> bool:
        """Elimina un cliente por su ID."""
        query = "DELETE FROM clientes WHERE id = ?"
        conn = self.db_manager.get_connection()
        exito = False
        try:
            cursor = conn.cursor()
            cursor.execute(query, (id_cliente,))
            conn.commit()
            exito = cursor.rowcount > 0
        except Exception as e:
            print(f"Error al eliminar cliente: {e}")
            exito = False
        return exito

    def modificar_cliente(self, cliente: Cliente) -> bool:
        """Modifica un cliente existente."""
        query = "UPDATE clientes SET nombre = ?, email = ?, saldo = ? WHERE id = ?"
        conn = self.db_manager.get_connection()
        exito = False
        try:
            cursor = conn.cursor()
            cursor.execute(query, (cliente.nombre, cliente.email, cliente.saldo, cliente.id))
            conn.commit()
            exito = cursor.rowcount > 0
        except Exception as e:
            print(f"Error al modificar cliente: {e}")
            exito = False
        return exito

    def listar_clientes(self) -> List[Cliente]:
        """Devuelve una lista con todos los clientes."""
        query = "SELECT id, nombre, email, saldo FROM clientes"
        conn = self.db_manager.get_connection()
        clientes = []
        try:
            cursor = conn.cursor()
            cursor.execute(query)
            rows = cursor.fetchall()
            for row in rows:
                clientes.append(Cliente(
                    id=row[0],
                    nombre=row[1],
                    email=row[2],
                    saldo=row[3]
                ))
        except Exception as e:
            print(f"Error al listar clientes: {e}")
        return clientes

    def obtener_cliente_por_id(self, id_cliente: int) -> Optional[Cliente]:
        """Obtiene un cliente por su ID."""
        query = "SELECT id, nombre, email, saldo FROM clientes WHERE id = ?"
        conn = self.db_manager.get_connection()
        cliente = None
        try:
            cursor = conn.cursor()
            cursor.execute(query, (id_cliente,))
            row = cursor.fetchone()
            if row:
                cliente = Cliente(
                    id=row[0],
                    nombre=row[1],
                    email=row[2],
                    saldo=row[3]
                )
        except Exception as e:
            print(f"Error al obtener cliente: {e}")
        return cliente
