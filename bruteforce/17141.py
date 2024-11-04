from collections import deque
from itertools import  combinations


n, m = map(int, input().split())

arr =list(list(map(int, input().split())) for _ in range(n))
delta = [[-1, 1, 0, 0], [0, 0, 1, -1]]
last = 2
remain = n * n
land = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 2:
            land.append((i,j))
        elif arr[i][j] == 1:
            remain -=1

ans = 9999
for viruses in combinations(land, m):
    temp = 0
    que = deque()
    visit = [[0] * n for _ in range(n)]
    for x, y in viruses:
        que.append((x, y))
        visit[x][y] = 1
    while que:
        x, y = que.popleft()
        time = visit[x][y]
        last = time
        temp += 1
        for i in range(4):
            dx, dy = x + delta[0][i], y + delta[1][i]
            if  0<= dx < n and 0<= dy < n and arr[dx][dy] != 1 and visit[dx][dy] == 0:
                visit[dx][dy] = time + 1
                que.append((dx, dy))
    ans = min(ans, ((last-1) if remain == temp else 9999))
    
print(-1 if ans == 9999 else ans)
