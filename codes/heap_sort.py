```
def heapify(arr, n, i):
    largest = i   # root is the largest initially
    left = 2 * i + 1
    right = 2 * i + 2
    
    # Check if left child exists and is greater than root
    if left < n and arr[i] < arr[left]:
        largest = left
    
    # Check if right child exists and is greater than root
    if right < n and arr[largest] < arr[right]:
        largest = right
    
    # If root isn't the largest, swap it with the larger one
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    
    # Build max-heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    
    # Extract elements from heap
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap root (max) to end of array
        heapify(arr, i, 0)              # Heapify reduced heap

test_array = [12, 11, 13, 5, 6, 7]
heap_sort(test_array)
print("Отсортированный массив:", test_array)
```
