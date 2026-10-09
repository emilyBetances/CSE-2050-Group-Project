from product import Product
from customer import Customer
from cart import ShoppingCart

class Store:
    def __init__(self):
        self.products = []
        self.customers = []

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
    

    

        
        