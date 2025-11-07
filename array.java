public class MaxFinder {
    public static int findMax(int[] arr, int n) {
        // Базис рекурсии: один элемент
        if (n == 1) {
            return arr[0];
        }
        
        // Рекурсивный вызов для первых n-1 элементов
        int maxOfRest = findMax(arr, n - 1);
        
        // Возвращаем максимум между последним элементом и максимумом остатка
        return (arr[n - 1] > maxOfRest) ? arr[n - 1] : maxOfRest;
    }

    public static void main(String[] args) {
        int[] arr = {3, 7, 2, 9, 1};
        int result = findMax(arr, arr.length);
        System.out.println("Максимальный элемент: " + result);  // Вывод: 9
    }
}
