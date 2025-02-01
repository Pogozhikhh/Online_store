import pytest

from src.Category import Category
from src.Product import Product


@pytest.fixture
def prod_1():
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


@pytest.fixture
def prod_2():
    return Product("Book", "paper", 200.0, 100)


@pytest.fixture
def cat_1():
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        ["Iphone", "Samsung"],
    )


@pytest.fixture
def cat_2():
    return Category("Принтеры", "Принтеры средство для печати", ["Canon", "aga", "reg"])
