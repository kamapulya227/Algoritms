#Создание списка 

#include <iostream>
#include <list> 

int main() {
    std::list<int> myList; // Создаем список целых чисел

    // Добавление элементов в конец списка
    myList.push_back(10);
    myList.push_back(20);
    myList.push_back(30);

    // Вставка элемента в начало списка
    myList.push_front(5);

    // Вывод элементов списка
    std::cout << "Содержимое списка: ";
    for (int val : myList) {
        std::cout << val << " ";
    }
    std::cout << std::endl; // Вывод: 5 10 20 30

    // Удаление элемента из начала списка
    myList.pop_front();

    std::cout << "После удаления первого элемента: ";
    for (int val : myList) {
        std::cout << val << " ";
    }
    std::cout << std::endl; // Вывод: 10 20 30

    return 0;
}

#Организация стека

#include <iostream>
#include <stack> 

int main() {
    std::stack<int> myStack; // Создаем стек целых чисел

    // Добавление элементов в стек
    myStack.push(100);
    myStack.push(200);
    myStack.push(300);

    std::cout << "Размер стека: " << myStack.size() << std::endl; // Вывод: 3

    // Удаление и вывод элемента с вершины стека
    std::cout << "Извлекаем элементы из стека:" << std::endl;
    while (!myStack.empty()) {
        std::cout << myStack.top() << " "; // Получаем элемент с вершины
        myStack.pop(); // Удаляем элемент с вершины
    }
    std::cout << std::endl; // Вывод: 300 200 100

    return 0;
}