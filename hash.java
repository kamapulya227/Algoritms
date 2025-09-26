import java.util.HashMap;

public class HashTableExample {
    public static void main(String[] args) {
        // Использование HashMap как хэш-таблицы
        HashMap<Integer, String> hashTable = new HashMap<>();

        // Добавление элементов
        hashTable.put(1, "One");
        hashTable.put(2, "Two");
        hashTable.put(3, "Three");

        // Поиск элемента
        String value = hashTable.get(2);
        System.out.println("Значение для ключа 2: " + value);

        // Проверка наличия ключа
        if (hashTable.containsKey(2)) {
            System.out.println("Ключ 2 существует");
        } else {
            System.out.println("Ключ 2 не существует");
        }
    }
