Алгоритмы поиска
Реализация на Python
Интерполяционный поиск
Код:
```
def interpolation_search(arr, lo, hi, x):
    if (lo <= hi and x >= arr[lo] and x <= arr[hi]):
        pos = lo + ((hi - lo) * (x - arr[lo]) // (arr[hi] - arr[lo]))
        
        if arr[pos] == x:
            return pos
        
        elif arr[pos] < x:
            return interpolation_search(arr, pos + 1, hi, x)
        
        else:
            return interpolation_search(arr, lo, pos - 1, x)
    return -1

sorted_arr = [10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 33, 35, 42, 47]
x = 18
index = interpolation_search(sorted_arr, 0, len(sorted_arr)-1, x)
if index != -1:
    print(f"Элемент найден на позиции: {index}")
else:
    print("Элемент не найден")
```