Алгоритмы структуры
Реализация на Python
1. Сортировка обменом (пузырьком)
Код:
```
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break

test_array = [64, 34, 25, 12, 22, 11, 90]
print("Исходный массив:", test_array)
bubble_sort(test_array)
print("Отсортированный массив:", test_array)
```
2. Сортировка Шелла 
Код:
```
def shell_sort(arr):
    n = len(arr)
    gap = n // 2  # Начальное расстояние
    
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j-gap] > temp:
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = temp
        gap //= 2  # Уменьшение расстояния

test_array = [12, 34, 54, 2, 3]
shell_sort(test_array)
print("Отсортированный массив:", test_array)
```
3. Пирамидальная сортировка
Код:
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