#Implementation of a red-black binary search tree.
class RedBlackBST(object):
    
    #RED = True
    #BLACK = False
    _root = None #Will serve as the root
    
    class Node(object):
        
        def __init__(self, key, value, n):
            self.key = key
            self.value = value
            #self.color = color #parent link color
            self.n = n #the count of the subtree
            
            #Get dealt with in time
            self.left = None
            self.right = None 
    
    # @classmethod
#     def _is_red(cls, node):
#         if node == None: return False
#         return node.color == cls.RED
#     
        
    def is_empty(self):
        return self.size() == 0
        
    def size(self):
        return _size(self._root)

    @staticmethod
    def _size(node):
        if node == None: return 0
        return node.n
    
    #Getting
    
    def contains(self, key):
        return self.get(key) != None
    
    def get(self, key):
        return _get(self._root, key)
    
    @staticmethod
    def _get(node, key):
        if node == None: return None
        if node.key < key:
            _get(node.left, key)
        elif node.key > key:
            _get(node.right, key)
        else:
            return node.value
        
    #Putting
    
    def put(self, key, val):
        if val == None:
            self.delete(key)
            return
        root = _put(root, key, val)
    
    @staticmethod        
    def _put(node, key, val):
        if node == None: return Node(key, val, 1)
        if node.key < key:
            node.left = put(node.left, key, val)
        elif node.key > key:
            node.right = put(node.right, key, val)
        else:
            node.val = val
        node.n = 1 + _size(node.left) + _size(node.right)
        return node
    
    
    
    