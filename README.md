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

## Код покрыт тестами 100%