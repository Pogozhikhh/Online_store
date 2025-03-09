# Домашняя работа Блока ООП
## Цель проекта
### Изучение концепции ООП и ее реализация


## Инструкция по установке
1. ### Клонируйте репозиторий:
```
https://github.com/Pogozhikhh/Online_store.git
```
## Домашняя работа 14_1
### Создание классов Product и Category с добавлением их атрибутов


### Класс Product

```
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

```

### Класс Category

```
class Category:
    """Создание класса Category"""

    name = str
    description = str
    products = list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(self.__products)

```

## Домашняя работа 14_2
### Изменение режима доступа для уже имеющихся классов Product и Category
### Добавление метода add_product
### Реализация геттера по выводу списка товаров
### Добавление метода new_product, возвращающий созданный объект класса из словаря
### Реализации сеттера для изменения цены не отрицательного значения

### Метод add_product
``` 
   def add_product(self, new_prod: Product):
        """Метод добавления нового продукта"""
        self.__products.append(new_prod)
        Category.category_count += 1
```

### Геттер products
```
@property
    def products(self):
        product_str = ""
        for product in self.__products:
            product_str = f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт."
        return product_str
```

### Метод new_product
```
@classmethod
    def new_product(cls, product_data):
        name = product_data.get("name")
        description = product_data.get("description")
        price = product_data.get("price")
        quantity = product_data.get("quantity")
        return cls(name, description, price, quantity)
```

### Сеттер смены цены
```
@price.setter
    def price(self, value: int):
        """Метод изменения атрибута price"""
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = value
```

## Домашняя работа 15_1
### Реализация методов __add__ и __str__ в классах

### Класс Product
```
    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        return self.__price * self.quantity + other.__price * other.quantity
```

### Класс Category

```
    def __str__(self):
        total_quanity = 0
        for product in self.__products:
            total_quanity += product.quantity
        return f"{self.name}, количество продуктов: {total_quanity} шт."
```
## Домашняя работа 16_1
### Создание классов наследников LawnGrass и Smartphone от класса Product

### Класс LawnGrass
```
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
```
### Класс Smartphone
```
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
```

## Домашняя работа 16_2
### Создание базового абстрактного класса и реализация класса миксин

### Базовый класс BaseProduct
```
class BaseProduct(ABC):

    @abstractmethod
    def __add__(self, other):
        pass

```

### Класс миксин MixinLog
```
class MixinLog:

    def __init__(self):
        print(repr(self))

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', '{self.description}', {self.price}, {self.quantity})"

```

## Домашняя работа 17_1
### Обработка исключений, которые могут возникать при обработке товаров, и уведомление с их помощью пользователя.

### Класс Product
```
    def __init__(self, name, description, price, quantity):
        if quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен.")
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__()
```

### Класс Category с добавлением метода middle_price
```
    def middle_price(self):
        """Метод подсчета среднего ценника всех товаров"""
        try:
            total_price = sum([product.price for product in self.__products])
            total_qua = sum([product.quantity for product in self.__products])
            return round(total_price / total_qua, 3)
        except ZeroDivisionError as e:
            print(e)
            return 0
```


## Код покрыт тестами 100%