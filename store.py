from product import Product
from customer import Customer
from cart import ShoppingCart
from order import Order
from order_queue import OrderQueue
from stack import Stack

class Store:
    def __init__(self):
        self.products = []
        self.customers = []
        self.orders = []
        self.order_queue = OrderQueue()
        self.order_history = Stack()
        self.order_counter = 0


    def add_product(self, product):
        if self.find_product(product.product_id) is not None:
            return False
        self.products.append(product)
        return True
        

    def find_product(self, product_id: str):
        for product in self.products:
            if product.product_id == str(product_id):
                return product
        return None
        

    def add_customer(self, customer):
        if self.find_customer(customer.customer_id) is not None:
            return False
        self.customers.append(customer)
        return True

    def find_customer(self,customer_id):
        for customer in self.customers:
            if customer.customer_id == customer_id:
             return customer
        return None
    

    def checkout(self, customer_id):
        customer = self.find_customer(customer_id)
        if customer is None:
            return None

        cart = customer.get_cart()

        if cart.is_empty():
            return None

        items = cart.get_items()

        self.order_counter += 1
        order_id = f"O{self.order_counter}"
        order = Order(order_id, customer, items)
        self.orders.append(order)
        self.order_queue.enqueue(order)
        cart.clear()
        return order

    def find_order(self, order_id):
        for order in self.orders:
            if order.get_id() == order_id:
                return order
        return None

    def get_orders(self):
        return list(self.orders)

    def process_next_order(self):
        order = self.order_queue.dequeue()
        if order is None:
            return None
        order.set_status("PROCESSING")
        self.order_history.push(order)
        return order

    def get_order_history(self):
        history = []
        current = self.order_history.items.head
        while current is not None:
            history.append(current.data)
            current = current.next
        return history

        
        