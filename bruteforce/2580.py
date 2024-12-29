def ok(x, y, now):
    for i in range(9):
        if arr[i][y] == now:
            return 0
        if arr[x][i] == now:
            return 0
    dx =  x- x%3
    dy = y - y%3
    for i in range(3):
        for j in range(3):
            if now == arr[dx + i][dy + j]:
                return 0
    return 1

def find(z):
    if z == len(zero):
        for i in range(9):
            print(*arr[i])
        exit()
    x, y = zero[z]
    for k in range(1, 10):
        if ok(x, y, k):
            arr[x][y] = k
            find(z + 1)
            arr[x][y] = 0

arr  = [list(map(int, input().split())) for _ in range(9)]
zero = []

for i in range(9):
    for j in range(9):
        if arr[i][j] == 0:
            zero.append((i, j))

find(0)
