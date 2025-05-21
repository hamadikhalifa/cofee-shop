from order import Order  # Order class is imported to maintain relationships

class Customer:
    """Defines a Customer within a coffee shop system."""
    all_customers = []    

    def __init__(self, name):
        self.name = name
        Customer.all_customers.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 15:
            self._name = value
        else:
            raise ValueError("Name should be a string with length between 1 to 15 characters.")

    def orders(self):
        """Return all orders placed by this customer."""
        return [order for order in Order.all_orders if order.customer == self]

    def coffees(self):
        """Return unique Coffee instances this Customer has ordered."""
        return list(set([order.coffee for order in self.orders()]))

    def create_order(self, coffee, price):
        """Create a new Order under this Customer."""
        order = Order(self, coffee, price)
        # Ensure the order is added to Order.all_orders if not handled in Order.__init__
        if not hasattr(Order, "all_orders"):
            Order.all_orders = []
        if order not in Order.all_orders:
            Order.all_orders.append(order)
        return order

    @classmethod
    def most_aficionado(cls, coffee):
        """
        Return the customer that has expensed the most on the coffee.
        Return None if no orders are found for the specified coffee.
        """
        all_orders = getattr(Order, "all_orders", [])
        if not all_orders:
            return None

        # Filter orders for the given coffee
        relevant_orders = [order for order in all_orders if order.coffee == coffee]
        if not relevant_orders:
            return None

        # Calculate spending per customer
        spending = {}
        for order in relevant_orders:
            spending[order.customer] = spending.get(order.customer, 0) + order.price

        # Find the customer with the highest spending
        max_customer = max(spending, key=spending.get, default=None)
        return max_customer