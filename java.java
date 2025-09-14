#Создание списка 

import java.util.ArrayList;
import java.util.List;

public class ListExample {
    public static void main(String[] args) {
        // Создаем пустой список строк
        List<String> fruits = new ArrayList<>();

        // Добавляем элементы в список
        fruits.add("Яблоко");
        fruits.add("Банан");
        fruits.add("Апельсин");

        // Печатаем список
        System.out.println("Список фруктов: " + fruits);

        // Получаем элемент по индексу
        System.out.println("Первый фрукт: " + fruits.get(0));

        // Удаляем элемент
        fruits.remove("Банан");
        System.out.println("Список после удаления банана: " + fruits);
    }
}

#Организация стека

import java.util.Stack;

public class StackExample {
    public static void main(String[] args) {
        // Создаем пустой стек целых чисел
        Stack<Integer> numberStack = new Stack<>();

        // Добавляем элементы на вершину стека
        numberStack.push(10);
        numberStack.push(20);
        numberStack.push(30);

        // Печатаем стек
        System.out.println("Стек чисел: " + numberStack);

        // Извлекаем элемент с вершины стека
        int topElement = numberStack.pop();
        System.out.println("Извлечен элемент: " + topElement);
        System.out.println("Стек после извлечения: " + numberStack);

        // Смотрим на верхний элемент, не извлекая его
        System.out.println("Верхний элемент: " + numberStack.peek());
    }
}