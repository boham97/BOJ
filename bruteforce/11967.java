import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static int[][] move = {
            {-1, 1, 0, 0},
            {0, 0, 1, -1}
    };
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        HashMap<Integer, ArrayList> switchHash = new HashMap<>();

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(bf.readLine());
            int[] input = new int[4];
            for (int j = 0; j < 4; j++) {
                input[j] = Integer.parseInt(st.nextToken());
            }
            int from = (input[0] - 1) * n + input[1] - 1;
            int to = (input[2] - 1) * n + input[3] - 1;

            ArrayList<Integer> valueList = new ArrayList<>();
            if (switchHash.containsKey(from)){
                valueList = switchHash.get(from);
            }
            valueList.add(to);
            switchHash.put(from, valueList);
        }

        int[][] visit = new int[n][n];

        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[] {0, 0});
        visit[0][0] = 2;    //dark 0 light 1 visit 2
        int answer = 1;
        while(! queue.isEmpty()){
            int[] now = queue.poll();
            int key = now[0] * n + now[1];
            if( switchHash.containsKey(key)){
                ArrayList<Integer> nowValueList = switchHash.get(key);
                for(int aAndB: nowValueList){
                    if(visit[aAndB/n][aAndB%n] == 0){
                        visit[aAndB/n][aAndB%n] = 1;
                        for (int i = 0; i < 4; i ++){
                            int[] next = new int[] {aAndB/n + move[0][i], aAndB%n + move[1][i]};
                            if ( next[0] >= 0 && next[0] < n && next[1] >= 0 && next[1] < n && visit[next[0]][next[1]] == 2){
                                visit[aAndB/n][aAndB%n] = 2;
                                queue.offer(new int[] {aAndB/n, aAndB%n});
                                break;
                            }
                        }
                        answer ++;
                    }
                }
            }
            for (int i = 0; i < 4; i ++){
                int[] next = new int[] {now[0] + move[0][i], now[1] + move[1][i]};
                if ( next[0] >= 0 && next[0] < n && next[1] >= 0 && next[1] < n && visit[next[0]][next[1]] == 1){
                    visit[next[0]][next[1]] = 2;
                    queue.offer(new int[] {next[0], next[1]});
                }

            }
        }
        System.out.println(answer);
    }
}