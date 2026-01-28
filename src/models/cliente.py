from dataclasses import dataclass

@dataclass
class Cliente:
    """Modelo para representar un cliente."""
    id: int
    nombre: str
    email: str
    saldo: float