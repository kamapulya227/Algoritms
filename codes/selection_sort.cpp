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
