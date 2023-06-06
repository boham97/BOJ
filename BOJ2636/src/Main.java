import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static List<ArrayList<Integer>> arr = new ArrayList<>();
    static int[] ans = new int[100];
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        for (int i = 0; i < N; i++) {
            arr.add(new ArrayList<>());
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                arr.get(i).add(Integer.parseInt(st.nextToken()));
            }
        }

        Deque<int[]> que = new LinkedList<>();
        que.offer(new int[] {0, 0});
        arr.get(0).set(0, 2);


        int[] now;
        int[][] del = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        int dx, dy;
        while (!que.isEmpty()) {
            now = que.poll();
            for (int i = 0; i < 4; i++) {
                dx = now[0] + del[i][0];
                dy = now[1] + del[i][1];
                if (0 <= dx && dx < N && 0 <= dy && dy < M) {
                    if (arr.get(dx).get(dy) == 0) {
                        arr.get(dx).set(dy, arr.get(now[0]).get(now[1]));
                        que.addFirst(new int[]{dx, dy});
                    }
                    if (arr.get(dx).get(dy) == 1) {
                        arr.get(dx).set(dy, arr.get(now[0]).get(now[1]) + 1);
                        que.offer(new int[]{dx, dy});
                        ans[arr.get(now[0]).get(now[1]) + 1]++;
                    }
                }
            }
        }
        for (int i = 99; i > 0; i--) {
            if (ans[i] > 0) {
                System.out.println(i - 2);
                System.out.println(ans[i]);
                break;
            }
        }
    }
}