from customer import Customer
from coffee import Coffee
from order import Order

# Sample data
latte = Coffee("Latte")
espresso = Coffee("Espresso")
alice = Customer("Alice")
bob = Customer("Bob")

# Place orders
Order(alice, latte, "large")
Order(alice, espresso, "small")
Order(bob, latte)

# Output
print("Alice's Coffees:", [c.name for c in alice.coffees()])
print("Latte Customers:", [c.name for c in latte.customers()])
