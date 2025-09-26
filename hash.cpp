#include <iostream>
#include <vector>

// Размер таблицы
const int TABLE_SIZE = 10;

// Структура для хранения пары ключ-значение
struct Pair {
    int key;
    int value;
};

// Хэш-функция
int hash(int key) {
    return key % TABLE_SIZE;
}

class HashTable {
private:
    std::vector<Pair> table;

public:
    HashTable() : table(TABLE_SIZE) {}

    // Вставка элемента
    void insert(int key, int value) {
        int index = hash(key);
        while (table[index].key != 0) { // Проверка на занятое место
            index = (index + 1) % TABLE_SIZE;
        }
        table[index] = {key, value};
    }

    // Поиск элемента
    int search(int key) {
        int index = hash(key);
        while (table[index].key != 0 && table[index].key != key) {
            index = (index + 1) % TABLE_SIZE;
        }
        return table[index].value;
    }

    // Вывод таблицы
    void print() {
        for (int i = 0; i < TABLE_SIZE; ++i) {
            if (table[i].key != 0) {
                std::cout << "Key: " << table[i].key << ", Value: " << table[i].value << std::endl;
            }
        }
    }
};

int main() {
    HashTable ht;
    ht.insert(1, 10);
    ht.insert(2, 20);
    ht.print();
    std::cout << "Search for key 1: " << ht.search(1) << std::endl;
    return 0;
}
