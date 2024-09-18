from customer import Customer
import pytest

## To test name validation, raise ValueError for not valid names
def test_customer_name_invalid_too_short():
    with pytest.raises(ValueError):
        Customer("")

def test_customer_name_invalid_too_long():
    with pytest.raises(ValueError):
        Customer("A very long name exceeding the limit")

## Test creating orders for a customer
def test_customer_orders():
    customer = Customer("Bob")
    assert len(customer.orders_list) == 0

