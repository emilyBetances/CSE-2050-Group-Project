from linked_list import LinkedList

class Stack:
    def __init__(self):
        self.items=LinkedList()
    def push(self,item):
        self.items.add_first(item)

    def pop(self):
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