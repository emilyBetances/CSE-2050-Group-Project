from node import Node

class LinkedList:
    def __init__(self):
        self.head = None 
        self.tail = None
        self.size = 0 

    def add_first(self,item):
        new_node = Node(item) 
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.size += 1

    def add_last(self,item):
        new_node = Node(item)

        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1 
        
    def remove_first(self):
        if not self.head:
            return None
        removed_data = self.head.data
        self.head = self.head.next 
        self._size -= 1
        if self._size == 0:
            self.tail = None
        return removed_data 

    def get_first(self):
        if not self.head:
            return None
        return self.head.data
    
    def is_empty(self) -> bool:
        return self._size == 0
    
    def size(self) -> int:
        return self._size