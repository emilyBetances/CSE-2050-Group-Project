import Product
import Customer
import ShoppingCart

class Store:
    def __init__(self):
        self.products = []
        self.customers = []

    def add_product(self, product):
        self.products.append(product)

    def find_product(self, product_id):
        for product in self.products:
            return self.products
        return None

    def add_customer(self, customer):
        for customer in self.customers:
            if customer.get_id() != customer:
                self.customer.append(customer)
                return True
        return False

    def find_customer(self,customer_id):
        for customer in self.customers:
            if customer.get_id() == customer_id:
             return customer_id
        return None


        
        