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