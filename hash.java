import java.util.HashMap;
import java.util.Map;

public class Main {
    public static void main(String[] args) {
        Map<String, Boolean> ht = new HashMap<>();
        ht.put("Фонарь", true);
        ht.put("Дверь", false);
        ht.put("Окно", true);

        for (var entry : ht.entrySet()) {
            System.out.println(entry.getKey() + ": " + (entry.getValue() ? "включен" : "выключен"));
        }
    }
}
