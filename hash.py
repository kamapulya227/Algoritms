class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * self.size

    def hash_function(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        while self.table[index] is not None and self.table[index][0] != key:
            index = (index + 1) % self.size
        self.table[index] = (key, value)

    def search(self, key):
        index = self.hash_function(key)
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            index = (index + 1) % self.size
        return None

# Пример использования
ht = HashTable(size=10)
ht.insert(1, 'value1')
ht.insert(2, 'value2')
print(ht.search(1))  # Вывод: value1
print(ht.search(2))  # Вывод: value2
