import random
    
def uniform_shuffle(arr):
    for i in range(0,len(arr)):
        r = random.randrange(0, i+1)
        swap = arr[r]
        arr[r] = arr[i]
        arr[i] = swap
    return arr