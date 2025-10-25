public class InterpolationSearch {
    public static int interpolationSearch(int[] arr, int target) {
        int low = 0;
        int high = arr.length - 1;
        
        while (low <= high && target >= arr[low] && target <= arr[high]) {
            // Формула интерполяции для предсказания позиции
            int pos = low + ((target - arr[low]) * (high - low)) / (arr[high] - arr[low]);
            
            if (arr[pos] == target)
                return pos;
            else if (arr[pos] < target)
                low = pos + 1;
            else
                high = pos - 1;
        }
        
        return -1;
    }
    
    public static void main(String[] args) {
        int[] arr = {10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 33, 35, 42, 47};
        int target = 18;
        
        int result = interpolationSearch(arr, target);
        
        if (result != -1)
            System.out.println("Элемент найден на позиции: " + result);
        else
            System.out.println("Элемент не найден");
    }
}