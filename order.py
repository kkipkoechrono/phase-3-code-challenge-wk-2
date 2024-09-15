
class Order:
    def __init__(self, customer, coffee, price):
        # Validate that the price is between 1.0 and 10.0
        if not (1.0 <= price <= 10.0):
            raise ValueError("Price must be between 1.0 and 10.0.")
        
        # Store customer, coffee, and price
        self._customer = customer
        self._coffee = coffee
        self._price = price

        # Add the order to the customer and coffee
        customer.add_order(self)
        coffee.add_order(self)

    @property
    def customer(self):
        return self._customer

    @property
    def coffee(self):
        return self._coffee

    @property
    def price(self):
        return self._price
