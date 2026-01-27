from dataclasses import dataclass
from src.models.item_venta import ItemVenta


@dataclass
class Venta:
    id: int
    precio_final: float
    estado: str
    items: list[ItemVenta] = field(default_factory=list)
