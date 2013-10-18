import random

class QuickSort(object):
    
    @classmethod
    def partition(cls, arr, low, high):
        
        i, j = low + 1, high
        
        while True:
            
            while arr[i] < arr[low]:
                i += 1
                if i >= high:
                    break
            
            while arr[j] > arr[low]:
                j -= 1
                if j <= low:
                    break
            
            if i >= j:
                break
            
            swap_els = arr[i]
            arr[i] = arr[j]
            arr[j] = swap_els
        
        swap_partition = arr[low]
        arr[low] = arr[j]
        arr[j] = swap_partition
        
        return j
            
        
    @classmethod
    def sort(cls, arr):
        for i in range(len(arr)):
            rand = random.randrange(0,i+1)
            
            swap = arr[rand]
            arr[rand] = arr[i]
            arr[i] = swap
        
        print arr
        
        cls.privateSort(arr, 0, len(arr) - 1)
        return arr
        
    @classmethod
    def privateSort(cls, arr, low, high):
        
        if high <= low:
            return 
        
        j = cls.partition(arr, low, high)
        cls.privateSort(arr, low, j-1)
        cls.privateSort(arr, j+1, high)