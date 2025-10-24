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

