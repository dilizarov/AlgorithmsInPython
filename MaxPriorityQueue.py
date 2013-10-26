#to be quite honest, this implementation seems rather redundant, but
#it seems to be the common way this is done (via sedgewick)

class MaxPQ(object):
    
    def __init__(self):
        self.pq = []
        self.no_of_el = 0
        
    def isEmpty(self):
        return self.no_of_el == 0
    
    def insert(self, key):
        self.pq.append(key)
        self.no_of_el += 1
    
    def delMax(self):
        try:
            maximum = 0
            n = self.no_of_el
            for i in range(1, n):
                if self.pq[maximum] < self.pq[i]:
                    maximum = i
        
            self.pq[maximum], self.pq[n-1] = self.pq[n-1], self.pq[maximum]
            self.no_of_el -= 1
            return self.pq.pop()
        except IndexError:
            print("The Priority Queue is empty! There is no max!")