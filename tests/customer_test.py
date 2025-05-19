import unittest
from customer import Customer
from coffee import Coffee
from order import Order

class TestCustomer(unittest.TestCase):
    def test_customer_can_have_orders(self):
        customer = Customer("Test")
        coffee = Coffee("Test Coffee")
        order = Order(customer, coffee)

        self.assertIn(order, customer.orders())
        self.assertIn(coffee, customer.coffees())

if __name__ == "__main__":
    unittest.main()
