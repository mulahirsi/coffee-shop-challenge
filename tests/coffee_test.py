import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.customer import Customer
from src.coffee import Coffee
from src.order import Order

class TestCoffee(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Customer A")
        self.coffee = Coffee("Espresso")
        self.order = Order(self.customer, self.coffee)

    def test_coffee_has_orders(self):
        # Add the order first
        self.coffee.add_order(self.order)
        self.assertIn(self.order, self.coffee.orders())

    def test_coffee_has_customers(self):
        # Add the order first
        self.coffee.add_order(self.order)
        self.assertIn(self.customer, self.coffee.customers())

if __name__ == "__main__":
    unittest.main()
