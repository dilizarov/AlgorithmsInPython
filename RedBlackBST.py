#Implementation of a red-black binary search tree.
class RedBlackBST(object):
    
    RED = True
    BLACK = False
    
    class Node(object):
        
        def __init__(self, key, value, color, n):
            self.key = key
            self.value = value
            self.color = color #parent link color
            self.n = n #the count of the subtree
    
    @classmethod
    def is_red(cls, node):
        if node == None: return False
        return node.color == cls.RED
    
    @classmethod
    def size(cls, node):
        if node == None: return 0
        return node.n
    
    