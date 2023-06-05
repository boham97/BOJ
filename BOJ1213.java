import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class BOJ1213 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String name = br.readLine();
        int[] arr = new int[26];
        int logic = 0;

        for (char c : name.toCharArray()) {
            arr[(int) c - 65]++;
        }
        StringBuilder sb = new StringBuilder();

        int even = -1;
        for (int i = 0; i < 26; i++) {
            for (int j = 0; j < arr[i]; j += 2) {
                sb.append((char) (i + 65));
            }
            if (arr[i] % 2 == 1) {
                if (even != -1) {
                    logic = 1;
                    break;
                }
                even = i;
                sb.delete(sb.length() - 1, sb.length());
            }
        }
        int isEven = 0;
        if (even != -1) {
            sb.append((char) (even + 65));
            isEven = 1;
        }
        for (int i = sb.length()-1-isEven; i > -1; i--) {
            sb.append(sb.toString().toCharArray()[i]);
        }
        if (logic == 1) {
            System.out.println("I'm Sorry Hansoo");
        } else {
            System.out.println(sb);
        }
    }
}