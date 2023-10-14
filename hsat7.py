from collections import deque
import sys
input = sys.stdin.readline

ans =0
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
n,m = map(int, input().split())
arr = list(list(map(int, input().split())) for _ in range(n))
visit = [[0] * m for  _ in range(n)]

locate = []
for i in range(m):
    a, b = map(int ,input().split())
    locate.append((a-1,b-1))
    if i == 0:
        p = (a-1, b-1)
        visit[a-1][b-1] = 1

def dfs(x,y,t):
    global ans
    if (x,y) == locate[t]:
        if t == m-1:
            ans += 1
            return
        t += 1
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0<= nx < n and 0 <= ny < n and arr[nx][ny] == 0 and visit[nx][ny] == 0:
            visit[nx][ny] = 1
            dfs(nx, ny, t)
            visit[nx][ny] = 0

dfs(locate[0][0], locate[0][1], 0)
print(ans)
