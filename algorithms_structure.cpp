Алгоритмы структуры
Реализация на C++
1. Сортировка выбором
Код:
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
2. Сортировка вставками
Код:
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
3. Быстрая сортировка
Код:
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