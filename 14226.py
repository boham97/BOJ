from collections import deque

N = int(input())

que = deque()
que.append((1,0))
visit = [[2000] * (2*N+1) for _ in range(2*N+1)]
visit[1][0] = 1
ans = 10000

while(que):
    x, y = que.popleft()

    if visit[x][y] > ans:
        continue
    if x == N:
        ans = visit[x][y]
    else:
        if visit[x][x] > visit[x][y] + 1:
            que.append((x,x))
            visit[x][x] = visit[x][y] + 1
        if y>0 and x+y < 2*N and visit[x+y][y] > visit[x][y] + 1:
            que.append((x+y,y))
            visit[x+y][y] = visit[x][y] + 1
        if x>1 and visit[x-1][y] > visit[x][y] + 1:
            que.append((x-1,y))
            visit[x-1][y] = visit[x][y] + 1
    
        
print(ans-1)
