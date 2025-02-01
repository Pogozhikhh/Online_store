def test_init(prod_1):
    assert prod_1.name == "Iphone 15"
    assert prod_1.description == "512GB, Gray space"
    assert prod_1.price == 210000.0
    assert prod_1.quantity == 8


def test_init_2(prod_2):
    assert prod_2.name == "Book"
    assert prod_2.description == "paper"
    assert prod_2.price == 200.0
    assert prod_2.quantity == 100
