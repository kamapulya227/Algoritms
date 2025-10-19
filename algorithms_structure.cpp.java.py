1. Сортировка выбором
Реализация на C++:
``` 
include <iostream>
using namespace std;
// Функция сортировки выбором
void selectionSort(int arr[], int n) {
    for (int i = 0; i < n - 1; ++i) { // Внешний цикл перебирает первые n-1 элементов
        int minIndex = i;              // Индексация минимального элемента
        
        // Внутренний цикл ищет минимум в неотсортированной части
        for (int j = i + 1; j < n; ++j) {
            if (arr[j] < arr[minIndex]) {
                minIndex = j;          // Обновление индекса минимума
            }
        }
        
        // Обмен найденного минимального элемента с текущим
        swap(arr[i], arr[minIndex]);
    }
}

// Основная функция для демонстрации
int main() {
    int arr[] = {64, 25, 12, 22, 11};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    cout << "Исходный массив:\n";
    for (int i = 0; i < n; ++i) {
        cout << arr[i] << " ";
    }
    cout << "\n\n";
    
    selectionSort(arr, n);
    
    cout << "Отсортированный массив:\n";
    for (int i = 0; i < n; ++i) {
        cout << arr[i] << " ";
    }
    cout << "\n";
    
    return 0;
}
```
2. Сортировка обменом (пузырьком)
Реализация на Python:
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
3. Сортировка вставками
Реализация на C++:
```
#include <iostream>
using namespace std;

// Основной метод сортировки вставками
void insertionSort(int arr[], int size) {
    int key, j;
    
    // Проходим по каждому элементу начиная со второго элемента
    for (int i = 1; i < size; ++i) {
        key = arr[i];   // Берём текущий элемент
        j = i - 1;      // Индекс предыдущего элемента
        
        /* Перемещаем все элементы слева от текущего,
           которые больше key, вправо */
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];     // Смещение большего элемента направо
            j--;
        }
        
        // Размещаем ключ на правильную позицию
        arr[j + 1] = key;
    }
}

// Тестовая программа
int main() {
    int arr[] = {64, 34, 25, 12, 22, 11, 90};
    int n = sizeof(arr)/sizeof(arr[0]);
    
    cout << "Исходный массив:\n";
    for (int i=0; i<n; i++)
        cout << arr[i] << " ";
    
    insertionSort(arr, n);
    
    cout << "\nОтсортированный массив:\n";
    for (int i=0; i<n; i++)
        cout << arr[i] << " ";
    
    return 0;
}
```
4. Сортировка слиянием 
Реализация на Java:
```
import java.util.Arrays;

public class MergeSortExample {
    public static void mergeSort(int[] arr) {
        if (arr.length > 1) {
            int mid = arr.length / 2;
            
            // Разделяем массив на две части
            int[] left = Arrays.copyOfRange(arr, 0, mid);
            int[] right = Arrays.copyOfRange(arr, mid, arr.length);
            
            // Рекурсивно сортируем обе части
            mergeSort(left);
            mergeSort(right);
            
            // Объединяем отсортированные части
            merge(arr, left, right);
        }
    }
    
    private static void merge(int[] arr, int[] left, int[] right) {
        int l = 0, r = 0, k = 0;
        while (l < left.length && r < right.length) {
            if (left[l] <= right[r])
                arr[k++] = left[l++];
            else
                arr[k++] = right[r++];
        }
        while (l < left.length)
            arr[k++] = left[l++];
        while (r < right.length)
            arr[k++] = right[r++];
    }
    
    public static void main(String[] args) {
        int[] array = {38, 27, 43, 3, 9, 82, 10};
        System.out.println("Исходный массив:");
        System.out.println(Arrays.toString(array));
        
        mergeSort(array);
        
        System.out.println("\nОтсортированный массив:");
        System.out.println(Arrays.toString(array));
    }
}
```
5. Сортировка Шелла 
Реализация на Python:
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
6. Быстрая сортировка
Реализация на C++:
```
#include <iostream>
using namespace std;

// Процедура разделения массива вокруг опорного элемента
int partition(int arr[], int low, int high) {
    int pivot = arr[high];                    // Опорный элемент
    int i = low - 1;                         // Начальное положение маленького элемента
    
    // Цикл перемещения элементов относительно опорного
    for (int j = low; j <= high - 1; ++j) {
        if (arr[j] < pivot) {                 // Если элемент меньше опорного
            i++;
            swap(arr[i], arr[j]);             // Обмен текущего и следующего
        }
    }
    
    // Поместить опорный элемент на свою финальную позицию
    swap(arr[i + 1], arr[high]);
    return i + 1;
}

// Основная процедура быстрой сортировки
void quickSort(int arr[], int low, int high) {
    if (low < high) {
        // Разделение массива и получение позиции опоры
        int pi = partition(arr, low, high);
        
        // Рекурсивно сортируем левую и правую части
        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}

// Основная функция для демонстрации
int main() {
    int arr[] = {10, 7, 8, 9, 1, 5};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    cout << "Исходный массив:\n";
    for (int i = 0; i < n; ++i) {
        cout << arr[i] << " ";
    }
    cout << "\n\n";
    
    quickSort(arr, 0, n - 1);
    
    cout << "Отсортированный массив:\n";
    for (int i = 0; i < n; ++i) {
        cout << arr[i] << " ";
    }
    cout << "\n";
    
    return 0;
}
```
7. Пирамидальная сортировка
Реализация на Python:
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