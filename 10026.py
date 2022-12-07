from collections import deque

N = int(input())
arr =[list(input()) for _ in range(N)]
visit = [[0]*N for _ in range(N)]
ans1 = 0
ans2 = 0
for i in range(N):
    for j in range(N):
        if not visit[i][j]:
            color = arr[i][j]
            que = deque()
            que.append([i,j])
            ans1 += 1
            visit[i][j] = 1
            while que:
                x, y = que.popleft()
                for dx, dy in [[x+1,y],[x-1,y],[x,y-1],[x,y+1]]:
                    if 0<=dx<N and 0<=dy<N and visit[dx][dy] == 0 and arr[dx][dy] == color:
                        visit[dx][dy] = 1
                        que.append([dx, dy])
visit = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not visit[i][j]:
            color = arr[i][j]
            que = deque()
            que.append([i,j])
            ans2 += 1
            visit[i][j] = 1
            while que:
                x, y = que.popleft()
                for dx, dy in [[x+1,y],[x-1,y],[x,y-1],[x,y+1]]:
                    if 0<=dx<N and 0<=dy<N and visit[dx][dy] == 0 and ((color == 'B' and arr[dx][dy] == color) or (color in ('R','G') and arr[dx][dy] != 'B') ):
                        visit[dx][dy] = 1
                        que.append([dx, dy])
print(ans1, ans2)