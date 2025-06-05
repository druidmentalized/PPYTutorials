from enum import Enum

class Currency(Enum):
    PLN = ("PLN", "zł")
    USD = ("USD", "$")
    EUR = ("EUR", "€")
    RUB = ("RUB", "₽")
    ARS = ("ARS", "$")

    def __init__(self, code, symbol) -> None:
        self.code = code
        self.symbol = symbol