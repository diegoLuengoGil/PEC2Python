from src.repository.inventario_repository import InventarioRepository
from src.models.producto import Producto
from typing import List, Optional

class InventarioService:
    def __init__(self, repositorio: InventarioRepository):
        self.repositorio = repositorio
    
    def agregar_producto(self, producto: Producto) -> bool:
        """Agrega un producto al inventario."""
        # Validaciones de negocio podrían ir aquí (ej. stock negativo inicial no permitido)
        resultado = False
        if producto.precio < 0:
            print("El precio no puede ser negativo.")
        elif producto.stock < 0:
            print("El stock no puede ser negativo.")
        else:
            resultado = self.repositorio.agregar_producto(producto)
        return resultado
    
    def eliminar_producto(self, id_producto: int) -> bool:
        """Elimina un producto por su ID."""
        return self.repositorio.eliminar_producto(id_producto)
    
    def modificar_producto(self, producto: Producto) -> bool:
        """Modifica un producto existente."""
        resultado = False
        if producto.precio < 0:
            print("El precio no puede ser negativo.")
        elif producto.stock < 0:
            print("El stock no puede ser negativo.")
        else:
            resultado = self.repositorio.modificar_producto(producto)
        return resultado

    def listar_productos(self) -> List[Producto]:
        """Obtiene la lista de todos los productos."""
        return self.repositorio.listar_productos()

    def obtener_producto(self, id_producto: int) -> Optional[Producto]:
        """Obtiene un producto por su ID."""
        return self.repositorio.obtener_producto_por_id(id_producto)
    