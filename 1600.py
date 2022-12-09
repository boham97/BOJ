from collections import deque

delta = [[1,0],[-1,0],[0,1],[0,-1]]
horse = [[-2,-1],[-2,1],[-1,-2],[-1,2],[1,-2],[1,2],[2,-1],[2,1]]
K = int(input())
M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visit = [[0]* M for _ in range(N)]
que = deque()
arr[0][0] = 2
visit[0][0] = K+1                                   #visit 전체가 0으로 되있으므로 1이면 방문가능
que.append([0, 0])
ans = 50000
while que:
    x,y = que.popleft()
    if arr[x][y] >= ans:                            #현재 정답보다 크면 탐색X
        continue
    if x==N-1 and y==M-1:
        if ans > arr[N-1][M-1]:
            ans = arr[N-1][M-1]
    for i in range(4):                             #원숭이처럼 가기 벽이 아니거나 방문가능하고 더빨리 갈수 있으면 방문
        dx, dy = x+delta[i][0], y+delta[i][1]
        if 0<=dx<N and 0<=dy<M and arr[dx][dy]!= 1 and (arr[dx][dy] > arr[x][y]+1 or visit[dx][dy] < visit[x][y]):
            que.append([dx,dy])
            arr[dx][dy] = arr[x][y] + 1
            visit[dx][dy] = visit[x][y]
    if visit[x][y]>1:                               # 말처럼 갈수 있으면
        for i in range(8):                          #더빨리 갈 수 있으면 ㄲㄲ, 말처럼 갔을때 해당위치에 저장된visit + 1보다 작아야 ㄲㄲ 저장된 visit와 같으면 갈 필요가 없다 => 같은 경우니까
            dx, dy = x+horse[i][0], y + horse[i][1]
            if 0<=dx<N and 0<=dy<M  and arr[dx][dy]!= 1 and (arr[dx][dy] > arr[x][y]+1 or visit[dx][dy] < visit[x][y]-1):
                que.append([dx,dy])
                arr[dx][dy] = arr[x][y] + 1
                visit[dx][dy] = visit[x][y] - 1

if ans == 50000:
    print(-1)
else:
    print(ans-2)