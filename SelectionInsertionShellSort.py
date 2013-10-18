def selection_sort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min]:
                min = j
        
        swap = arr[min]
        arr[min] = arr[i]
        arr[i] = swap
    
    return arr
    
def insertion_sort(arr):
    for i in range(len(arr)):
        for j in range(i, 0, -1):
            if arr[j] < arr[j-1]:
                swap = arr[j-1]
                arr[j-1] = arr[j]
                arr[j] = swap
            else:
                break
    return arr
    
def shell_sort(arr):
    n = len(arr)
    h = 1
    while h < n/3:
        h = 3*h + 1
    
    while h >= 1:
        for i in range(h, n):
            for j in range(i, h-1, -h):
                if arr[j] < arr[j - h]:
                    swap = arr[j-h]
                    arr[j-h] = arr[j]
                    arr[j] = swap
                else:
                    break
        h = h/3
    
    return arr