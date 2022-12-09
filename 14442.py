from collections import deque
from sys import stdin
delta = [[1,0],[-1,0],[0,1],[0,-1]]
N, M, K = map(int, stdin.readline().split())
arr = [list(map(int, list(stdin.readline()))) for _ in range(N)]
arrcopy = [arr[i][:] for i in range(N)]
visit = [[0]* M for _ in range(N)]
que = deque()
arr[0][0] = 2
visit[0][0] = K+1                                   #visit 전체가 0으로 되있으므로 1이면 방문가능
que.append([0, 0])
ans = 1000*1000 + 10

while que:
    x,y = que.popleft()
    if arr[x][y] >= ans:                            #현재 정답보다 크면 탐색X
        continue
    if x==N-1 and y==M-1:
        if ans > arr[N-1][M-1]:
            ans = arr[N-1][M-1]
    for i in range(4):                             #그냥 탐색                           
        dx, dy = x+delta[i][0], y+delta[i][1]
        if 0<=dx<N and 0<=dy<M:
            if arrcopy[dx][dy]!= 1 and (arr[dx][dy] > arr[x][y]+1 or visit[dx][dy] < visit[x][y]):
                que.append([dx,dy])
                arr[dx][dy] = arr[x][y] + 1
                visit[dx][dy] = visit[x][y]
            if arrcopy[dx][dy]== 1 and visit[dx][dy]<visit[x][y]-1: #벽이고 방문시 남은 능력 횟수가 더 크면 방문!       
                que.append([dx,dy])
                arr[dx][dy] = arr[x][y] + 1
                visit[dx][dy] = visit[x][y] - 1
     

if ans == 1000010:
    print(-1)
else:
    print(ans-1)