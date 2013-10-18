class LinkedStack(object):
    
    class Node(object):
        def __init__(self, item = None, next = None):
            self.item = item
            self.next = next
    
    def __init__(self):
        self.first = None

    def isEmpty(self):
        return self.first == None
    
    def push(self, item):
        oldfirst = self.first
        self.first = Node(item, oldfirst)
        
    def pop(self):
        item = self.first.item
        self.first = self.first.next
        return item