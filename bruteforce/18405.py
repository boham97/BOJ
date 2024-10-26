from collections import deque

n, k = map(int, input().split())

arr = list(list(map(int, input().split())) for _ in range(n))
s, x, y = map(int, input().split())
x, y = x - 1, y - 1

que = []

for i in range(n):
    for j in range(n):
        if arr[i][j]:
            que.append((i,j,0))

que.sort(key = lambda x: arr[x[0]][x[1]])

que =deque(que)

delta = [-1, 1, 0, 0]


while que:
    vx, vy, t = que.popleft()
    v = arr[vx][vy]
    if t == s or arr[x][y]: break
    for i in range(4):
        dx, dy = vx + delta[i], vy + delta[3 - i]
        if 0 <= dx < n and 0 <= dy < n and not arr[dx][dy]:
            arr[dx][dy] = v
            que.append((dx, dy, t + 1))


print(arr[x][y])
