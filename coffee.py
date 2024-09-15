# coffee.py

class Coffee:
    def __init__(self, name):
        # Validate that the coffee name is at least 3 characters long
        if isinstance(name, str) and len(name) >= 3:
            self._name = name
        else:
            raise ValueError("Coffee name must be at least 3 characters long.")

        # Create an empty list to store orders for this coffee
        self.orders_list = []

    @property
    def name(self):
        return self._name

    def add_order(self, order):
        # Add the order to the coffee's order list
        self.orders_list.append(order)

    def orders(self):
        # Return all orders for this coffee
        return self.orders_list

    def customers(self):
        # Return a set of unique customers who ordered this coffee
        return set(order.customer for order in self.orders_list)

    def num_orders(self):
        # Return the number of orders for this coffee
        return len(self.orders_list)

    def average_price(self):
        # Calculate the average price of the coffee based on its orders
        if len(self.orders_list) == 0:
            return 0
        total_price = sum(order.price for order in self.orders_list)
        return total_price / len(self.orders_list)
