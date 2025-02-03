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

    def __str__(self):
        total_quanity = 0
        for product in self.__products:
            total_quanity += product.quantity
        return f"{self.name}, количество продуктов: {total_quanity} шт."


    @property
    def product_list(self):
        product_str = ""
        for product in self.__products:
            product_str += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт."
        return product_str

    def add_product(self, new_prod: Product):
        """Метод добавления нового продукта"""
        self.__products.append(new_prod)
        Category.category_count += 1
