from dataclasses import dataclass, field
from models.item_venta import ItemVenta

@dataclass
class Venta:
    """Modelo para representar una venta."""
    id: int
    total: float
    estado: str
    cliente_id: int
    items: list[ItemVenta] = field(default_factory=list)
