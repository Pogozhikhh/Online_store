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
    assert category_tv.products == '55" QLED 4K, 123000.0 руб. Остаток: 7 шт.'


def test_category(category_smart, product_4):
    was_products = Category.product_count
    category_smart.add_product(product_4)
    category_smart.add_product(new_prod)
    assert Category.product_count == was_products
