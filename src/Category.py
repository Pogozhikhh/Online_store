from src.Product import Product


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

    @property
    def products(self):
        products = ""
        for product in self.__products:
            products += str(product)
        return products

    def middle_price(self):
        """Метод подсчета среднего ценника всех товаров"""
        try:
            total_price = sum([product.price for product in self.__products])
            total_qua = sum([product.quantity for product in self.__products])
            return round(total_price / total_qua, 3)
        except ZeroDivisionError as e:
            print(e)
            return 0

    def __str__(self):
        total_quanity = 0
        for product in self.__products:
            total_quanity += product.quantity
        return f"{self.name}, количество продуктов: {total_quanity} шт."

    @property
    def product_list(self):
        product_str = ""
        for product in self.__products:
            product_str += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return product_str

    def add_product(self, new_prod: Product):
        """Метод добавления нового продукта"""
        if isinstance(new_prod, Product):
            try:
                if new_prod.quantity == 0:
                    raise ValueError("Товар с нулевым количеством не может быть добавлен")
            except ValueError as e:
                print(f"Ошибка {e}")
            else:
                self.__products.append(new_prod)
                Category.product_count += 1
                print(f"Товар '{new_prod.name}' успешно добавлен.")
            finally:
                print("Обработка добавления товара завершена.")
        else:
            raise TypeError()
