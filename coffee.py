from order import Order  # Import Order class for relationship handling


class Coffee:

    all_coffees = []

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) >= 3:
            self._name = value
        else:
            raise ValueError("Coffee name must be a string with at least 3 characters.")

    def __init__(self, name): 
        self.name = name 
        Coffee.all_coffees.append(self)

    def orders(self):
        """Return all orders for this coffee as a list."""
        # Use getattr in case Order.all_orders is not defined
        all_orders = getattr(Order, 'all_orders', [])
        return [order for order in all_orders if order.coffee == self]

    def customers(self):
        """Return a list of unique customers who ordered this coffee."""
        return list({order.customer for order in self.orders()})

    def num_orders(self):
        """Return total number of times this coffee has been ordered (int)."""
        return len(self.orders())

    def average_price(self):
        """Return average price (float) of all orders for this coffee, or 0 if none."""
        orders = self.orders()
        if not orders:
            return 0.0
        total = sum(order.price for order in orders)
        return total / len(orders)