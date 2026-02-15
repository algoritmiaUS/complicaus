import java.io.*;
import java.util.*;

public class E {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // Leer n, ignorando líneas vacías
        String line;
        while ((line = br.readLine()) != null && line.trim().isEmpty());

        if (line == null) return; // no input
        int n = Integer.parseInt(line.trim());

        Map<String, Integer> count = new HashMap<>();

        for (int i = 0; i < n; i++) {
            String t;
            while ((t = br.readLine()) != null && t.trim().isEmpty());
            if (t == null) break;
            count.put(t, count.getOrDefault(t, 0) + 1);
        }

        String winner = "NONE";
        for (Map.Entry<String, Integer> e : count.entrySet()) {
            int v = e.getValue();
            String k = e.getKey();
            if (v > n - v) { // mayoría
                winner = k;
                break;
            }
        }

        System.out.println(winner);
    }
}
