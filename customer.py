
class Customer:
    def __init__(self, name):
        ## Validate that the name is between 1 and 15 characters
        self._name = None  
        self.name = name  
        ## Create an empty list to store orders
        self.orders_list = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        ## Check that name is a string and 1-15 letters long
        if isinstance(value, str) and 1 <= len(value) <= 15:
            self._name = value
        else:
            raise ValueError("Name must be a string between 1 and 15 characters.")

    def add_order(self, order):
        ## Add the order to the list of orders
        self.orders_list.append(order)

    def orders(self):
        ## Return all orders this customer has made
        return self.orders_list

    def coffees(self):
        ## Return a set of unique Coffee instances from the orders
        return set(order.coffee for order in self.orders_list)
