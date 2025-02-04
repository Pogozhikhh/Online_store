class Product:
    """Создание класса Product"""

    name = str
    description = str
    price = float
    quantity = int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт.\n"

    def __add__(self, other):
        return self.__price * self.quantity + other.__price * other.quantity

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value: int):
        """Метод изменения атрибута price"""
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = value

    @classmethod
    def new_product(cls, product_data):
        name = product_data.get("name")
        description = product_data.get("description")
        price = product_data.get("price")
        quantity = product_data.get("quantity")
        return cls(name, description, price, quantity)


class Smartphone(Product):
    """Создание дочернего класса Product"""

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other):
        if type(other) is Smartphone:
            return self.quantity + other.quantity
        elif isinstance(other, int):
            return self.quantity + other
        else:
            raise TypeError


class LawnGrass(Product):
    """Создание дочернего класса Product"""

    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other):
        if type(other) is LawnGrass:
            return self.quantity + other.quantity
        elif isinstance(other, int):
            return self.quantity + other
        else:
            raise TypeError
