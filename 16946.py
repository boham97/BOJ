import sys
from collections import deque
input = sys.stdin.readline
delta = [1, -1, 0, 0]
now = 1
color = [0]
def bfs(x, y):
    global now
    arr[x][y] = 1
    q = deque()
    q2 = deque()
    q.append((x, y))
    q2.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            dx, dy = x + delta[i], y + delta[3- i]
            if 0 <= dx < n and 0 <= dy < m and arr[dx][dy] == 0:
                arr[dx][dy] = 1
                q.append((dx, dy))
                q2.append((dx, dy))
    color.append(len(q2))
    while q2:
        x, y = q2.popleft()
        cnt[x][y] = now
    now += 1

n, m = map(int, input().split())
arr = list(list(map(int, list(input().rstrip()))) for _ in range(n))
cnt = list([0] * m for _ in range(n))
ans = list([0] * m for _ in range(n))
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            continue
        bfs(i, j)
        
for i in range(n):
    for j in range(m):
        if cnt[i][j] != 0:
            continue
        side = set()
        for k in range(4):
            di, dj = i + delta[k], j + delta[3- k]
            if 0 <= di < n and 0 <= dj < m:
                side.add(cnt[di][dj])
        for c in side:
            ans[i][j] += color[c]
        ans[i][j] += 1

for i in range(n):
    for j in range(m):
        print(ans[i][j]%10, end = '')
    print()
    
        
