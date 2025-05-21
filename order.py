class Order:
    all_orders = []

    def __init__(self, customer, coffee, price):
        from customer import Customer
        from coffee import Coffee

        if not isinstance(customer, Customer):
            raise TypeError("customer must be a Customer instance")
        if not isinstance(coffee, Coffee):
            raise TypeError("coffee must be a Coffee instace")
        if not (isinstance(price, (int, float)) and 3.0 <= float(price) <= 11.0):
            raise ValueError("price must be a float between 3.0 and 11.0")

        self._customer = customer
        self._coffee = coffee
        self._price = float(price)

        Order.all_orders.append(self)

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, value):
        from customer import Customer
        if not isinstance(value, Customer):
            raise ValueError("customer must be a Customer instance")
        self._customer = value

    @property
    def coffee(self):
        return self._coffee

    @coffee.setter
    def coffee(self, value):
        from coffee import Coffee
        if not isinstance(value, Coffee):
            raise ValueError("coffee must be a Coffee instance")
        self._coffee = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not (isinstance(value, (int, float)) and 3.0 <= float(value) <= 11.0):
            raise ValueError("price must be a float between 3.0 and 11.0")
        self._price = float(value)

    @property
    def purchased(self):
        return self._purchased

    def mark_as_purchased(self):
        self._purchased = True

    @classmethod
    def delete_order(cls, order):
        if order in cls.all_orders:
            cls.all_orders.remove(order)

    @classmethod
    def all(cls):
        return cls.all_orders
