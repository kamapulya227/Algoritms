#include <iostream>
#include <vector>
using namespace std;

int find_max(const vector<int>& arr, int n) {
    // Базис рекурсии: один элемент
    if (n == 1) {
        return arr[0];
    }
    
    // Рекурсивный вызов для первых n-1 элементов
    int max_of_rest = find_max(arr, n - 1);
    
    // Возвращаем максимум между последним элементом и максимумом остатка
    return (arr[n - 1] > max_of_rest) ? arr[n - 1] : max_of_rest;
}

int main() {
    vector<int> arr = {3, 7, 2, 9, 1};
    int result = find_max(arr, arr.size());
    cout << "Максимальный элемент: " << result << endl;  // Вывод: 9
    return 0;
}
