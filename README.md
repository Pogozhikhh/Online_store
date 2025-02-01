# Домашняя работа Блока ООП
## Цель проекта
### Изучение концепции ООП и ее реализация


## Инструкция по установке
1. ### Клонируйте репозиторий:
```
https://github.com/Pogozhikhh/Online_store.git
```

## Домашняя работа 14_1
### Создание классов Product и Category с их атрибутами

### Класс Product

```
class Product:
    name = str
    description = str
    price = float
    quantity = int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

```

### Класс Category

```
class Category:
    name = str
    description = str
    products = list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products
        Category.category_count += 1
        Category.product_count += len(products)

```