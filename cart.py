from product import Product

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_product(self, product):
        self.items.append(product)

    def remove_product(self, product_id):
        for product in self.items:
            if product.get_id() == product_id:
                self.items.remove(product)
                return True
        return False

    def get_items(self):
        return self.items

    def calculate_total(self):
        total = 0.0
        for product in self.items:
            total += product.get_price()
        return total

    def is_empty(self):
        return len(self.items) == 0

    def clear(self):
        self.items.clear()