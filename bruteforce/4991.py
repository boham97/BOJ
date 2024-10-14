from collections import deque

delta = [-1, 1, 0, 0]

def update_cost(index):
    x, y = point[index]
    visit = [[0] * n for _ in range(m)]
    visit[x][y] = 1
    que = deque()
    que.append((x, y))

    while que:
        x, y = que.popleft()
        for i in range(4):
            dx, dy = x + delta[i], y + delta[3 - i]
            if 0 <= dx < m and 0 <= dy < n and visit[dx][dy] == 0 and arr[dx][dy] != 'x':
                visit[dx][dy] = visit[x][y] + 1
                que.append((dx, dy))
    for j in range(len(point)):
        px, py = point[j]
        if visit[px][py] != 0:
            cost[index][j] = visit[px][py] - 1


def dfs(now, temp):
    global ans
    if visit2[now] == len(point):
        if temp < ans:
            ans = temp
        return
    for i in range(len(point)):
        if visit2[i] != 0: continue
        visit2[i] = visit2[now] + 1
        dfs(i, temp + cost[now][i])
        visit2[i] = 0

inf = 9876543210
while(1):
    ans = inf
    n, m = map(int, input().split())
    if n == 0 and m == 0: break

    arr = [list(input()) for _ in range(m)]
    start = 0
    point = []
    for i in range(m):
        for j in range(n):
            if arr[i][j] == '*' or arr[i][j] == 'o':
                point.append((i,j))
                if arr[i][j] == 'o':
                    start = len(point) - 1

    cost = [[inf] * len(point) for _ in range(len(point))]
    for i in range(len(point)):
        update_cost(i)

    visit2 = [0] * len(point)
    visit2[start] = 1

    dfs(start, 0)
    print(ans if ans < inf else -1)
