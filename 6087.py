from collections import deque

delta = [-1, 1, 0, 0]
w, h = map(int, input().split())

arr = list(list(input()) for _ in range(h))

turn = [[10000] * w for _ in range(h)]
que = deque()

for i in range(h):
    for j in range(w):
        if arr[i][j] == 'C':
            que.append((i,j))
            turn[i][j] = 1
ans_x, ans_y = que.pop()
turn[ans_x][ans_y] = 10000

while que:
    x, y = que.popleft()
    for i in range(4):
        dx, dy = x + delta[i], y + delta[3 - i]
        while 0 <= dx < h and 0 <= dy < w and arr[dx][dy] != '*':
            if turn[dx][dy] > turn[x][y] + 1:
                turn[dx][dy] = turn[x][y] + 1
                que.append((dx,dy))
            dx, dy = dx + delta[i], dy + delta[3 - i]
    arr[x][y] = '*'
print(turn[ans_x][ans_y] - 2)

            
