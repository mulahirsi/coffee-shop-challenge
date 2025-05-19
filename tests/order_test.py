import unittest
from customer import Customer
from coffee import Coffee
from order import Order

class TestOrder(unittest.TestCase):
    def test_order_initialization(self):
        customer = Customer("Bob")
        coffee = Coffee("Latte")
        order = Order(customer, coffee, "large")

        self.assertEqual(order.customer, customer)
        self.assertEqual(order.coffee, coffee)
        self.assertEqual(order.size, "large")

if __name__ == "__main__":
    unittest.main()
