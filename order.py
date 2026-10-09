from product import Product
from customer import Customer

class Order:

    def __init__(self, order_id:str, customer:Customer, items:list):
        self.order_id = order_id
        self.customer = customer 
        self.items = list(items)
        self.status = "PENDING"

    def get_id(self):
        return self.order_id

    def get_customer(self):
        return self.customer

    def get_items(self):
        return self.items.copy()

    def get_status(self):
        return self.status

    def set_status(self,status:str):
        valid_statuses = {"PENDING","PROCESSING","COMPLETED"}
        if status not in valid_statuses: 
            raise ValueError(f"invalid status: {status}")
        self.status = status 


    def calculate_total(self):
        total = 0.0
        for product in self.items:
            total += product.get_price()
        return total 

        
