import pytest

from src.Product import Product


@pytest.fixture
def prod_1():
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


def test_init(prod_1):
    assert prod_1.name == "Iphone 15"
    assert prod_1.description == "512GB, Gray space"
    assert prod_1.price == 210000.0
    assert prod_1.quantity == 8
