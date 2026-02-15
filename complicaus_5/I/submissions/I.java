import java.util.*;
import java.util.stream.*;

public class Paul {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.nextLine();

        String[] names = new String[n];
        for (int i = 0; i < n; i++) {
            names[i] = sc.nextLine();
        }
        Arrays.sort(names, Comparator.comparing(
            s -> s.substring(
                IntStream.range(0, s.length())
                .filter(i -> Character.isUpperCase(s.charAt(i)))
                .findFirst()
                .getAsInt()
            )
        ));
        for (String s: names) {
            System.out.println(s);
        }
    }
}
