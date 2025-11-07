def find_max(arr, n):
    # Базис рекурсии: если массив из одного элемента
    if n == 1:
        return arr[0]
    
    # Рекурсивный вызов: ищем максимум в первых n-1 элементах
    max_of_rest = find_max(arr, n - 1)
    
    # Возвращаем максимум между первым элементом и максимумом остатка
    return arr[n - 1] if arr[n - 1] > max_of_rest else max_of_rest


# Пример использования
arr = [3, 7, 2, 9, 1]
result = find_max(arr, len(arr))
print("Максимальный элемент:", result)  # Вывод: 9
