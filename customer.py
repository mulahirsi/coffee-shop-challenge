class Customer:
    def __init__(self, name):
        self.name = name
        self._orders = []

    def add_order(self, order):
        self._orders.append(order)

    def orders(self):
        return self._orders

    def coffees(self):
        return list(set(order.coffee for order in self._orders))
