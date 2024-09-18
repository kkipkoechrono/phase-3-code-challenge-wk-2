from coffee import Coffee
import pytest

# Test for coffee
def test_coffee_name():
    coffee = Coffee("Latte")
    assert coffee.name == "Latte"

# Test name validation (at least 3 characters)
def test_coffee_name_invalid_too_short():
    with pytest.raises(ValueError):
        Coffee("Es")

# Test number of orders and average price
def test_coffee_orders():
    coffee = Coffee("Espresso")
    assert len(coffee.orders()) == 0 
     #there should be no orders at first
