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
    assert str(product_1) == 'Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.'