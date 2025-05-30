class InvalidPriceError(Exception):
    pass

class Product:
    def __init__(self, name: str, price: float):
        if price < 0:
            raise InvalidPriceError("Price must be over 0!")
        self.name = name
        self.price = price

product_good = Product("PiProduct", 3.14)
product_bad = Product("MinusPiProduct", -3.14)