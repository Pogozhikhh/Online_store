from itertools import product
from test.conftest import category_smart, category_tv

import pytest

from src.Category import Category
from src.Product import Product

new_prod = Product.new_product(
    {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5,
    }
)


def test_category_tv(category_tv, product_4):
    assert category_tv.name == "Телевизоры"
    assert category_tv.description == (
        "Современный телевизор, который позволяет наслаждаться просмотром," " станет вашим другом и помощником"
    )
    assert category_tv.products == '55" QLED 4K, 123000.0 руб. Остаток: 7 шт.\n'


def test_category(category_tv, product_4):
    was_products = Category.product_count
    category_tv.add_product(product_4)
    category_tv.add_product(new_prod)
    assert Category.product_count == was_products + 2


def test_count_quanity(category_smart):
    test = str(category_smart)
    assert test == "Смартфоны, количество продуктов: 27 шт."


def test_add_different_class(category_smart):
    with pytest.raises(TypeError):
        category_smart.add_product("Nothing")

def test_middle_price():
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)

    category1 = Category("Смартфоны", "Категория смартфонов", [product1, product2])
    assert category1.middle_price() == 30000.0

def test_middle_price_empy():
    category = Category("Category", "Description", [])
    assert category.middle_price() == 0.0

def test_add_product_with_zero_quantity():
    with pytest.raises(ValueError) as e:
        test_prod = Product("Бракованный товар", "Неверное количество", 1000.0, 0)
        Category.add_product(test_prod)
    assert (str(e.value), "Товар с нулевым количеством не может быть добавлен")
