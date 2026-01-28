from dataclasses import dataclass


@dataclass
class Producto:
    """Modelo para representar un producto."""
    id: int
    nombre: str
    descripcion: str
    precio: float
    stock: int
    categoria: str
