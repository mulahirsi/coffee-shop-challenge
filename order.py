class Order:
    def __init__(self, customer, coffee, size="medium"):
        self.customer = customer
        self.coffee = coffee
        self.size = size

        customer.add_order(self)
        coffee.add_order(self)

    def __repr__(self):
        return f"{self.customer.name} ordered a {self.size} {self.coffee.name}"
