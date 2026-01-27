from dataclasses import dataclass


@dataclass
class Producto:
    id: int
    nombre: str
    descripcion: str
    precio: float
    stock: int
    categoria: str
