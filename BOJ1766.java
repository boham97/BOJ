import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        ArrayList<Integer> ans = new ArrayList<>();

        ArrayList<ArrayList<Integer>> arr = new ArrayList<ArrayList<Integer>>();
        int[] income = new int[N+1];
        for(int i = 0; i <=N; i ++){
            arr.add(new ArrayList<Integer>());
        }
        for(int i = 0; i < M; i++){
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            arr.get(a).add(b);
            income[b] ++;
        }

        PriorityQueue<Integer> hq = new PriorityQueue<>();

        for (int i = 1; i <= N; i++ ){
            if(income[i] == 0){
                hq.offer(i);
            }
        }

        while (!hq.isEmpty()){
            int now = hq.poll();
            ans.add(now);

            for(int next:arr.get(now)){
                income[next]--;
                if (income[next] == 0){
                    hq.offer(next);
                }
            }
        }
        StringBuilder sb = new StringBuilder();
        for(int a: ans){
            sb.append(a).append(' ');
        }
        System.out.println(sb);
    }
}