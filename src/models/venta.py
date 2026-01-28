from dataclasses import dataclass, field
from src.models.item_venta import ItemVenta
from typing import List

@dataclass
class Venta:
    """Modelo para representar una venta."""
    id: int
    total: float
    estado: str
    items: List[ItemVenta] = field(default_factory=list)
