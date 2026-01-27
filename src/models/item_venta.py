from dataclasses import dataclass


@dataclass
class ItemVenta:
    id: int
    venta_id: int
    producto_id: int
    cantidad: int
    subtotal: float
