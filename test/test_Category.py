import pytest

from src.Category import Category


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


def test_init1(cat_1):
    assert cat_1.name == "Смартфоны"
    assert (
        cat_1.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert cat_1.products == ["Iphone", "Samsung"]


def test_category_count1(cat_1):
    assert cat_1.category_count == 1


def test_product_count1(cat_1):
    assert cat_1.product_count == 2


def test_init2(cat_2):
    assert cat_2.name == "Принтеры"
    assert cat_2.description == "Принтеры средство для печати"
    assert cat_2.products == ["Canon", "aga", "reg"]


def test_category_count2(cat_2):
    assert cat_2.category_count == 1


def test_product_count2(cat_2):
    assert cat_2.product_count == 3
