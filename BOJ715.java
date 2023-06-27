import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int ans = 0;
        int N = Integer.parseInt(br.readLine());
        PriorityQueue<Integer> pq = new PriorityQueue<>();

        for (int i = 0; i < N; i ++){
            pq.add(Integer.parseInt(br.readLine()));
        }

        while(pq.size() > 1){
            int num1 = pq.poll();
            int num2 = pq.poll();
            int temp = num1 + num2;
            ans += temp;
            pq.add(temp);
        }

        System.out.println(ans);
    }

}