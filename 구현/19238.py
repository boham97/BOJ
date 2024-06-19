from collections import deque

delta = [[-1, 1, 0, 0], [0, 0, 1, -1]]
def goHere():
    global fuel
    visit = [[0] * n for _ in range(n)]
    x, y = taxi[0], taxi[1]
    visit[x][y] = 1
    que = deque()
    que.append((x,y))
    candidate = []
    while que:
        x, y = que.popleft()
        if n * x + y in here:
            candidate.append((x, y))
        for i in range(4):
            dx, dy = x + delta[0][i], y + delta[1][i]
            if 0 <= dx < n and 0 <= dy < n and arr[dx][dy] == 0 and visit[dx][dy] == 0:
                visit[dx][dy] = visit[x][y] + 1
                que.append((dx, dy))

    candidate.sort(key = lambda x: (visit[x[0]][x[1]], x, y))
    if candidate and fuel >= visit[candidate[0][0]][candidate[0][1]] - 1:
        x, y = candidate[0]
        taxi[0], taxi[1] = x, y
        fuel -= visit[x][y] - 1
        return True
    else:
        return False

def goThere():
    global fuel
    visit = [[0] * n for _ in range(n)]
    x, y = taxi[0], taxi[1]
    visit[x][y] = 1
    que = deque()
    que.append((x,y))
    num = here[n*x + y]
    del here[n* x + y]
    toX, toY = there[num]
    while que:
        x, y = que.popleft()
        if x == toX and y == toY:
            if visit[x][y] and fuel >= visit[x][y] - 1:
                fuel += visit[x][y] - 1
                taxi[0], taxi[1] = x, y
                return True
            break
        for i in range(4):
            dx, dy = x + delta[0][i], y + delta[1][i]
            if 0 <= dx < n and 0 <= dy < n and arr[dx][dy] == 0 and visit[dx][dy] == 0:
                visit[dx][dy] = visit[x][y] + 1
                que.append((dx, dy))
    return False


n, m , fuel = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
taxi = list(map(int, input().split()))
taxi = [taxi[0] -1, taxi[1] -1]
here = {}
there = {}
for i in range(m):
    a, b, c , d = map(int, input().split())
    here[n*(a-1) + b - 1] = i
    there[i] = (c - 1, d - 1)
ans = 0

while fuel > 0 and ans < m:
    if not goHere():
        break
    if not goThere():
        break
    ans += 1

print(fuel if ans == m else -1)
