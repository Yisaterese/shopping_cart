from shopping_cart import shopping_cart
import pytest
@pytest.fixture

def cart():
    return shopping_cart(5)

def test_can_add_items_to_cart(cart):
    cart.add("apple")
    assert cart.size() == 1

def test_item_can_add(cart):
    cart.add("apple")
    assert "apple"in  cart.get_items(cart)

def test_item_are_in_range(cart):
    for i in range(6):
        cart.add("apple")

def test_can_get_total_price(cart):
    cart.add("apple")
    cart.add("orange")
    dict_price = {"apple":200,"orange":50}
    assert cart.get_get_total_price(dict_price) == 250







