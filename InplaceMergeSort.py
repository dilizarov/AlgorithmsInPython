import random
import pdb

class Merge(object):
    
    @classmethod
    def merge(cls, arr, low, mid, high, i, j):

        i, j = low, mid+1
        # entries, moves = 0, 0
        count = 0
        for index in range(low, high):
            if arr[i] > arr[j]:
                arr[index], arr[j] = arr[j], arr[index]
                
                if i <= mid and j != high:
                    i, j = j, j + 1
                elif j != high:
                    j += 1
                elif i <= mid:
                    i = j
            
                # if index <= mid:
                #     entries += 1
                #     moves += 1
            
                if index == i:
                    i += 1
            else:
                if i <= mid:
                    i += 1
                else:         
                    arr[index], arr[i] = arr[i], arr[index]
                    # if index <= mid:
#                         entries += 1
                    # if index <= mid:
        #                 count += 1
                    if j - i > 1 or index == i:
                        i += 1
            
                    # if j - i == 1 and mid:
                    #     i = j - count
                    #     count = 0
            # if index >= mid and entries == moves*2:
#                 i = j - moves
#                 entries, moves = 0, 0
        
            # if index == mid and i != mid + 1:
#                 i = mid + 1
#                 mid = i + (high - i)//2
#                 j = mid + 1
        
        #pdb.set_trace()
        return arr
    
    @classmethod
    def privateSort(cls, arr, low, high, i, j):
        if high <= low:
            return
    
        mid = low + (high - low) // 2
        
        cls.privateSort(arr, low, mid, i, j)
        cls.privateSort(arr, mid+1, high, i, j)
        cls.merge(arr, low, mid, high, i, j)
    
    @classmethod
    def sort(cls, arr):
        i, j = 0,0
        cls.privateSort(arr, 0, len(arr)-1, i, j)
        return arr
        
man = [8,4,2,1,6,4,3,6,2,12, 13]
mang = [random.randrange(0,12) for x in range(10)]
b = Merge.sort(mang)
print(b)