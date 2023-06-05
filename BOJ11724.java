import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;


public class Main {
    static List<ArrayList<Integer>> arr = new ArrayList<>();
    static int[] visit;
    static int N, ans;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        for (int i = 0; i < N + 1; i++) {
            arr.add(new ArrayList<>());
        }

        visit = new int[N + 1];
        ans = 0;


        while (M-- > 0) {

            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());

            arr.get(u).add(v);
            arr.get(v).add(u);
        }

        for (int i = 1; i < N + 1; i++) {
            if (visit[i] == 0) {
                BFS(i);
                ans++;
            }
        }
        System.out.println(ans);
    }

    static void BFS(int i) {
        Queue<Integer> queue = new LinkedList<>();
        queue.offer(i);
        visit[i] = 1;
        while ( !queue.isEmpty()) {
            int now = queue.poll();
            for (int j = 0; j < arr.get(now).size(); j++) {
                int newValue = arr.get(now).get(j);
                if (visit[newValue] == 0) {
                    queue.offer(arr.get(now).get(j));
                    visit[arr.get(now).get(j)] = 1;
                }
            }
        }
    }
}