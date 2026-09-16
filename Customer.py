import ShoppingCart

class Customer:
    def __init__(self, customer_id, name):
        self.customer_id = customer_id
        self.name = name
        self.cart = ShoppingCart()

    def get_id(self):
        return self.customer_id
    def get_name(self):
        return self.name

    def get_cart(self):
        return self.cart
    