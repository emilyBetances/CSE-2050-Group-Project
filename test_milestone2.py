import unittest

from order import Order
from linked_list import LinkedList
from stack import Stack
from order_queue import OrderQueue
from store import Store
from customer import Customer
from product import Product

class TestOrder(unittest.TestCase):
    def test_initial_status(self):
        customer = Customer("C1", "Alice")
        order = Order("01", customer, [])
        self.assertEqual(order.get_status(), "PENDING")

        self.assertEqual(order.get_id(), "01")

        self.assertIs(order.get_customer(), customer)

    def test_change_status(self):
        customer = Customer("C1", "Alice")
        order = Order("01", customer, [])
        order.set_status("PROCESSING")
        self.assertEqual(order.get_status(), "PROCESSING")

    def test_cart_independence(self):
        customer = Customer("C1", "Alice")
        product = Product("P1", "Mouse", 25.0)
        items = [product]
        order = Order("01", customer, items)
        items.clear()
        self.assertEqual(len(order.get_items()), 1)
        self.assertAlmostEqual(order.calculate_total(), 25.0)

class TestLinkedList(unittest.TestCase):
    def test_empty_list(self):
        linked = LinkedList()
        self.assertTrue(linked.is_empty())
        self.assertEqual(linked.size(), 0)
        self.assertIsNone(linked.get_first())

    def test_add_first(self):
        linked = LinkedList()
        linked.add_first(10)
        linked.add_first(20)

        self.assertEqual(linked.get_first(), 20)
        self.assertEqual(linked.size(), 2)

    def test_add_last(self):
        linked = LinkedList()
        linked.add_last(10)
        linked.add_last(20)

        self.assertEqual(linked.remove_first(), 10)
        self.assertEqual(linked.remove_first(), 20)

    def test_remove_first(self):
        linked = LinkedList()
        linked.add_first(50)
        self.assertEqual(linked.remove_first(), 50)
        self.assertTrue(linked.is_empty())
        self.assertIsNone(linked.remove_first())

class TestStack(unittest.TestCase):
    def test_lifo(self):
        stack = Stack()
        stack.push(10)
        stack.push(20)
        stack.push(30)

        self.assertEqual(stack.pop(), 30)
        self.assertEqual(stack.pop(), 20)
        self.assertEqual(stack.pop(), 10)

    def test_peek(self):
        stack = Stack()
        stack.push(100)
        self.assertEqual(stack.peek(), 100)
        self.assertEqual(stack.size(), 1)

    def test_empty_pop(self):
        stack = Stack()
        self.assertIsNone(stack.pop())
        self.assertTrue(stack.is_empty())

class TestOrderQueue(unittest.TestCase):
    def test_fifo(self):
        queue = OrderQueue()
        queue.enqueue(10)
        queue.enqueue(20)
        queue.enqueue(30)

        self.assertEqual(queue.dequeue(), 10)
        self.assertEqual(queue.dequeue(), 20)
        self.assertEqual(queue.dequeue(), 30)

    def test_peek(self):
        queue = OrderQueue()
        queue.enqueue(100)

        self.assertEqual(queue.peek(), 100)
        self.assertEqual(queue.size(), 1)

    def test_empty_dequeue(self):
        queue = OrderQueue()
        self.assertIsNone(queue.dequeue())
        self.assertTrue(queue.is_empty())


class TestStore(unittest.TestCase):
    def setUp(self):
        self.store = Store()
        self.customer = Customer("C1", "Alice")
        self.product = Product("P1", "Mouse", 25.0)

        self.store.add_customer(self.customer)
        self.store.add_product(self.product)

    def test_checkout(self):
        cart = self.customer.get_cart()
        cart.add_product(self.product)
        order = self.store.checkout("C1")
        self.assertIsNotNone(order)
        self.assertEqual(order.get_status(), "PENDING")
        self.assertEqual(len(self.store.get_orders()), 1)

    def test_checkout_clears_cart(self):
        cart = self.customer.get_cart()
        cart.add_product(self.product)
        order = self.store.checkout("C1")
        self.assertIsNotNone(order)
        self.assertTrue(cart.is_empty())

    def test_empty_checkout(self):
        order = self.store.checkout("C1")
        self.assertIsNone(order)
        self.assertEqual(len(self.store.get_orders()), 0)

    def test_process_order(self):
        cart = self.customer.get_cart()
        cart.add_product(self.product)
        order = self.store.checkout("C1")
        processed = self.store.process_next_order()
        self.assertIs(processed, order)
        self.assertEqual(processed.get_status(), "PROCESSING")

    def test_order_history(self):
        cart = self.customer.get_cart()
        cart.add_product(self.product)
        first = self.store.checkout("C1")
        cart.add_product(self.product)
        second = self.store.checkout("C1")
        self.store.process_next_order()
        self.store.process_next_order()
        history = self.store.get_order_history()
        self.assertEqual(len(history), 2)
        self.assertIs(history[0], second)
        self.assertIs(history[1], first)
        self.assertEqual(len(self.store.get_order_history()), 2)

        
if __name__ == "__main__":
    unittest.main()