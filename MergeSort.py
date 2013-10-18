class Merge(object):
    
    @classmethod
    def merge(cls, arr, holder, low, mid, high):

        for k in range(low, high + 1):
            holder[k] = arr[k]
        i = low
        j = mid + 1
        for k in range(low, high + 1):
            if i > mid and holder[j] != None:
                arr[k] = holder[j]
                j += 1
            elif j > high and holder[i] != None:
                arr[k] = holder[i]
                i += 1
            elif holder[j] < holder[i] and holder[j] != None:
                arr[k] = holder[j]
                j += 1
            elif holder[i] != None:
                arr[k] = holder[i]
                i += 1
                
        return arr
    
    @classmethod
    def privateSort(cls, arr, holder, low, high):
        if high <= low:
            return
    
        mid = low + (high - low) / 2
        
        cls.privateSort(arr, holder, low, mid)
        cls.privateSort(arr, holder, mid + 1, high)
        cls.merge(arr, holder, low, mid, high)
    
    @classmethod
    def sort(cls, arr):
        aux = [None] * len(arr)
        cls.privateSort(arr, aux, 0, len(arr) - 1)
        return arr