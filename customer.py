
class Customer:
    def __init__(self, name):
        # Validate that the name is between 1 and 15 characters
        self._name = None  # A placeholder for the name, we'll set it via property
        self.name = name  # This uses the property setter for validation

        # Create an empty list to store orders
        self.orders_list = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        # Check that the name is a string and 1-15 characters long
        if isinstance(value, str) and 1 <= len(value) <= 15:
            self._name = value
        else:
            raise ValueError("Name must be a string between 1 and 15 characters.")

    def add_order(self, order):
        # Add the order to the list of orders for this customer
        self.orders_list.append(order)

    def orders(self):
        # Return all orders this customer has made
        return self.orders_list

    def coffees(self):
        # Return a set of unique Coffee instances from the orders
        return set(order.coffee for order in self.orders_list)
