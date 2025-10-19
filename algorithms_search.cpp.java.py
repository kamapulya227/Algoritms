1. Линейный поиск 
Реализация на C++:
```
#include <iostream>
using namespace std;

// Функция линейного поиска
int linearSearch(int arr[], int size, int target) {
    for (int i = 0; i < size; ++i) {
        if (arr[i] == target) {
            return i;                       // Вернуть индекс найденного элемента
        }
    }
    return -1;                             // Элемента нет в массиве
}

// Основная функция для демонстрации
int main() {
    int arr[] = {3, 5, 2, 7, 9, 1, 4};
    int size = sizeof(arr) / sizeof(arr[0]);
    int target = 7;
    
    int index = linearSearch(arr, size, target);
    
    if (index != -1) {
        cout << "Элемент найден на позиции: " << index << endl;
    } else {
        cout << "Элемент не найден." << endl;
    }
    
    return 0;
}
```
2. Бинарный поиск 
Реализация на Java:
```
public class BinarySearch {
    public static int binarySearch(int[] array, int target) {
        int left = 0;
        int right = array.length - 1;
        
        while (left <= right) {
            int mid = left + (right - left) / 2;
            
            if (array[mid] == target) {
                return mid;  // Найден элемент
            }
            
            if (target < array[mid]) {
                right = mid - 1;  // Поиск в левой половине
            } else {
                left = mid + 1;   // Поиск в правой половине
            }
        }
        return -1;  // Элемент не найден
    }
    
    public static void main(String[] args) {
        int[] sortedArray = {1, 3, 5, 7, 9, 11, 13, 15, 17, 19};
        int target = 7;
        
        int result = binarySearch(sortedArray, target);
        if (result != -1) {
            System.out.println("Элемент найден на позиции: " + result);
        } else {
            System.out.println("Элемент не найден");
        }
    }
}
```
3. Интерполяционный поиск
Реализация на Python:
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
4. Фибоначчиевый поиск
Реализация на Java:
```
public class FibonacciSearch {
    public static int fibonacciSearch(int[] arr, int x) {
        int fibMm2 = 0; // (m-2)'е число Фибоначчи
        int fibMm1 = 1; // (m-1)'е число Фибоначчи
        int fibM = fibMm2 + fibMm1; // Число Фибоначчи >= длина массива
        
        while (fibM < arr.length) {
            fibMm2 = fibMm1;
            fibMm1 = fibM;
            fibM = fibMm2 + fibMm1;
        }
        
        int offset = -1;
        
        while (fibM > 1) {
            int i = Math.min(offset + fibMm2, arr.length - 1);
            
            if (arr[i] < x) {
                fibM = fibMm1;
                fibMm1 = fibMm2;
                fibMm2 = fibM - fibMm1;
                offset = i;
            } else if (arr[i] > x) {
                fibM = fibMm2;
                fibMm1 = fibMm1 - fibMm2;
                fibMm2 = fibM - fibMm1;
            } else {
                return i;
            }
        }
        
        if (fibMm1 != 0 && offset + 1 < arr.length && arr[offset + 1] == x) {
            return offset + 1;
        }
        return -1;
    }
    
    public static void main(String[] args) {
        int[] sortedArr = {10, 22, 35, 40, 45, 50, 80, 82, 85, 90, 100};
        int searchElement = 85;
        int foundIndex = fibonacciSearch(sortedArr, searchElement);
        if (foundIndex != -1) {
            System.out.println("Элемент найден на позиции: " + foundIndex);
        } else {
            System.out.println("Элемент не найден");
        }
    }
}
```
