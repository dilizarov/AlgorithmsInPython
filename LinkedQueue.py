class LinkedQueue(object):
    
    class Node(object):
        def __init__(self, item = None, next = None):
            self.item = item
            self.next = next
        
    def __init__(self):
        self.first = None
        self.last = None
        
    def isEmpty(self):
        return self.first == None
        
    def enqueue(self, item):
        oldlast = self.last
        self.last = Node(item)
        if self.isEmpty():
            self.first = self.last
        else:
            oldlast.next = self.last
        
    def dequeue(self):
        item = self.first.item
        self.first = self.first.next
        if self.isEmpty():
            self.last = None
        
        return item
