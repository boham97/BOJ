from collections import deque
dx = [-1, 1, 0 , 0]
dy = [0, 0, 1, -1]
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visit = [[0] *M for _ in range(N)]
ans = [0] * 52
que = deque()
que.append((0,0))
visit[0][0] = 1

while que:
    i, j = que.popleft()
    for k in range(4):
        x = i+ dx[k]
        y = j + dy[k]
        if 0<= x < N and 0 <= y < M and visit[x][y] == 0:
            if arr[x][y] == 0:
                visit[x][y] = visit[i][j]
                que.appendleft((x,y))
            elif arr[x][y] == 1:
                visit[x][y] = visit[i][j] + 1
                que.append((x,y))
                ans[visit[x][y]] += 1

for i in range(51, 0, -1):
    if ans[i] != 0:
        print(i - 1)
        print(ans[i])
        break
