from linked_list import LinkedList 
class OrderQueue:
    def __init__(self):
        self.items = LinkedList()

    def enqueue(self,item):
        self.items.add_last(item)


    def dequeue(self):
        if self.is_empty():
            return None 
        return self.items.remove_first()

    def peek(self):
        if self.is_empty():
            return None 
        return self.items.get_first()
    
    def is_empty(self):
        return self.items.is_empty()
    
    def size(self):
        return self.items.size()