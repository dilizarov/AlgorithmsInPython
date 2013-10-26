class BinaryHeap(object):
    
    def __init__(self):
        self.pq = [None] #The heap is an index 1-based heap.
        self.n = 0 #n = no. of elements
        
    def isEmpty(self):
        return self.n == 0
    
    def insert(self, key):
        self.n += 1
        self.pq.insert(self.n, key)
        self.swim(self.n)
        
    def less(self, i, j):
        return self.pq[i] < self.pq[j]
        
    def exch(self, i, j):
        self.pq[i], self.pq[j] = self.pq[j], self.pq[i]
    
    def swim(self, k):
        while k > 1 and self.less(k//2, k):
            self.exch(k, k//2)
            k //= 2
    
    def sink(self, k):
        while 2*k <= self.n:
            j = 2*k
            if j < self.n and self.less(j, j+1):
                j += 1
            if not self.less(k, j): 
                break
            
            self.exch(k, j)
            k = j
    
    def delMax(self):
        try:
            if self.isEmpty(): raise IndexError
            max = self.pq[1]
            self.exch(1, self.n)
            self.n -= 1
            self.sink(1)
            return max
        except IndexError:
            print("The Binary Heap is empty! There is no max!")
            
    def sort(self):
        while self.n > 1:
            self.exch(1, self.n)
            self.n -= 1
            self.sink(1)
        
        return [self.pq[i] for i in range(1, len(self.pq))]
    