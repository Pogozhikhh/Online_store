from pyexpat.errors import messages

import pytest

from src.Product import Product

new_prod = Product.new_product(
    {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5,
    }
)


def test_init(product_2):
    assert product_2.name == "Iphone 15"
    assert product_2.description == "512GB, Gray space"
    assert product_2.price == 210000.0
    assert product_2.quantity == 8


def test_price():
    new_prod.price = 0
    assert new_prod.price == 180000.0
    new_prod.price = 100.0
    assert new_prod.price == 100.0


def test_str(product_1):
    assert str(product_1) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"


def test_add_not_int(grass_1):
    with pytest.raises(TypeError):
        result = grass_1 + "1"


def test_add_other_class(grass_1, product_1):
    with pytest.raises(TypeError):
        result = grass_1 + product_1


def test_mixin_product(capsys):
    Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)

    message = capsys.readouterr()
    assert message.out.strip() == "Product('Samsung Galaxy S23 Ultra', '256GB, Серый цвет, 200MP камера', 180000.0, 5)"


def test_add_zero_quanity():
    with pytest.raises(ValueError) as e:
        Product("Бракованный товар", "Неверное количество", 1000.0, 0)

    assert str(e.value) == "Товар с нулевым количеством не может быть добавлен."
