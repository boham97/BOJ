from collections import deque
import sys
input = sys.stdin.readline
inf =  1000
delta = [-1, 1, 0, 0]
n = int(input())
arr =list(list(input().rstrip()) for _ in range(n))
pos = dict()
x, y = 0, 0
for i in range(n):
    for j in range(n):
        if arr[i][j] == '#':
            x, y = i, j
            break
    if x + y != 0:
        break
visit = [[inf] * n for _ in range(n)]
q = deque()
q.append((x,y))
arr[x][y] = '*'
visit[x][y] = 0
while q:
    x, y = q.popleft()
    if arr[x][y] =='#':
        print(visit[x][y] - 1)
        break
    for k in range(4):
            dx, dy = x + delta[k], y + delta[3 - k]
            while 0 <= dx < n and 0<= dy < n and arr[dx][dy] != '*':
                if (arr[dx][dy] == '#' or arr[dx][dy] == '!') and (visit[dx][dy] > visit[x][y] + 1):
                    visit[dx][dy] = visit[x][y] + 1
                    q.append((dx,dy))
                dx, dy = dx + delta[k], dy + delta[3 - k]                                                     
