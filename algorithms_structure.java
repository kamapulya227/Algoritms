Алгоритмы структуры
Реализация на Java
Сортировка слиянием
Код:
```
import java.util.Arrays;

public class MergeSortExample {
    public static void mergeSort(int[] arr) {
        if (arr.length > 1) {
            int mid = arr.length / 2;
            
            // Разделяем массив на две части
            int[] left = Arrays.copyOfRange(arr, 0, mid);
            int[] right = Arrays.copyOfRange(arr, mid, arr.length);
            
            // Рекурсивно сортируем обе части
            mergeSort(left);
            mergeSort(right);
            
            // Объединяем отсортированные части
            merge(arr, left, right);
        }
    }
    
    private static void merge(int[] arr, int[] left, int[] right) {
        int l = 0, r = 0, k = 0;
        while (l < left.length && r < right.length) {
            if (left[l] <= right[r])
                arr[k++] = left[l++];
            else
                arr[k++] = right[r++];
        }
        while (l < left.length)
            arr[k++] = left[l++];
        while (r < right.length)
            arr[k++] = right[r++];
    }
    
    public static void main(String[] args) {
        int[] array = {38, 27, 43, 3, 9, 82, 10};
        System.out.println("Исходный массив:");
        System.out.println(Arrays.toString(array));
        
        mergeSort(array);
        
        System.out.println("\nОтсортированный массив:");
        System.out.println(Arrays.toString(array));
    }
}
```