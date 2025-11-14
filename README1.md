# Хусяинова Камиля. УИБО-10-24
# Вариант 5. Покрытие множеств с жадным алгоритмом
## Задача: реализовать жадный ln(n)-аппроксимационный алгоритм для задачи о покрытии множеств.
## 1. Код на языке Python:
```
def set_cover(universe, subsets):
    """
    Жадный алгоритм для задачи покрытия множеств.
    Возвращает выбранные подмножества и общее количество элементов в покрытии.
    """
    uncovered = set(universe)
    selected_subsets = []
    subset_names = []
    
    # Создаем список имен подмножеств
    names = [f"S{i+1}" for i in range(len(subsets))]
    
    while uncovered and subsets:
        # Находим подмножество, которое покрывает наибольшее число непокрытых элементов
        best_subset = None
        best_cover = set()
        best_index = -1
        best_name = ""
        
        for i, subset in enumerate(subsets):
            current_cover = uncovered.intersection(subset)
            if len(current_cover) > len(best_cover):
                best_cover = current_cover
                best_subset = subset
                best_index = i
                best_name = names[i]
        
        if best_subset:
            selected_subsets.append(best_subset)
            subset_names.append(best_name)
            uncovered -= best_cover
            # Удаляем выбранное подмножество
            subsets.pop(best_index)
            names.pop(best_index)
    
    # Вычисляем общее количество уникальных элементов в покрытии
    covered_elements = set()
    for subset in selected_subsets:
        covered_elements.update(subset)
    
    return selected_subsets, subset_names, len(covered_elements)

# Ввод данных от пользователя
print("Задача о покрытии множеств")
print("Введите универсальное множество (через пробел):")
universe_input = input().split()
universe = set(map(int, universe_input))

print(f"\nУниверсум: {universe}")
print("\nВведите подмножества. Для завершения ввода введите 'end'")

subsets = []
subset_num = 1

while True:
    print(f"Введите подмножество S{subset_num} (через пробел) или 'end' для завершения:")
    subset_input = input().strip()
    
    if subset_input.lower() == 'end':
        break
    
    subset_elements = list(map(int, subset_input.split()))
    subsets.append(set(subset_elements))
    print(f"S{subset_num} = {set(subset_elements)} добавлено")
    subset_num += 1

# Запуск алгоритма
if subsets:
    selected_subsets, selected_names, total_elements = set_cover(universe, subsets.copy())

    # Вывод результатов
    print("\n" + "="*50)
    print("РЕЗУЛЬТАТЫ:")
    print("="*50)
    
    print("\nВыбранные подмножества:")
    for name, subset in zip(selected_names, selected_subsets):
        print(f"{name}: {subset}")

    print(f"\nОбщее количество элементов в покрытии: {total_elements}")
    print(f"Количество выбранных подмножеств: {len(selected_subsets)}")

    # Проверка покрытия
    covered = set()
    for subset in selected_subsets:
        covered.update(subset)

    if covered == universe:
        print("Все элементы универсума покрыты")
    else:
        print("Не все элементы покрыты")
        print(f"Не покрыты: {universe - covered}")
else:
    print("Не введено ни одного подмножества!")
```
## 2. Анализ алгоритма
### Как работает алгоритм:
Программа запускается с ввода данных от пользователя - универсального множества и подмножеств. В функции ```set_cover()``` используется жадная стратегия:
1. Инициализация: создается множество ```uncovered``` для отслеживания непокрытых элементов
2. Основной цикл: пока есть непокрытые элементы и доступные подмножества:
- Внутренний цикл проходит по всем подмножествам и находит то, которое покрывает максимальное количество непокрытых элементов
- Выбранное подмножество добавляется в результат, а покрытые элементы удаляются из ```uncovered```
- Выбранное подмножество удаляется из дальнейшего рассмотрения
3. Завершение: вычисляется общее количество покрытых элементов и возвращается результат

## 3. Временная сложность
O(m² × n)
## 4. 
