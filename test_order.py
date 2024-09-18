from order import Order
from customer import Customer
from coffee import Coffee
import pytest

# Test for order creation
def test_order_creation():
    customer = Customer("Charlie")
    coffee = Coffee("Cappuccino")
    order = Order(customer, coffee, 5.0)
    assert order.customer == customer
    assert order.coffee == coffee
    assert order.price == 5.0

# Test price validation
def test_order_invalid_price():
    customer = Customer("Charlie")
    coffee = Coffee("Cappuccino")
    with pytest.raises(ValueError):
        Order(customer, coffee, 15.0) 

    with pytest.raises(ValueError):
        Order(customer, coffee, 0.5) 