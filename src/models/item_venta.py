from dataclasses import dataclass


@dataclass
class ItemVenta:
    """Modelo para representar un item de venta."""
    id: int
    venta_id: int
    producto_id: int
    cantidad: int
    subtotal: float
