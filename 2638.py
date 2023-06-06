import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 1, 0 , 0]
dy = [0, 0, 1, -1]
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visit = [[0] *M for _ in range(N)]
ans = [0] * 200
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
                temp = 0
                for l in range(4):
                    x2 = x+ dx[l]
                    y2 = y + dy[l]
                    if 0<= x2 < N and 0 <= y2 < M and 0 < visit[x2][y2] <= visit[i][j]:
                        temp += 1
                if temp > 1:
                    visit[x][y] = visit[i][j] + 1
                    que.append((x,y))
                    ans[visit[x][y]] += 1

for i in range(199, 0, -1):
    if ans[i] != 0:
        print(i - 1)
        break
