Алгоритмы поиска
Реализация на C++
Линейный поиск
Код:
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