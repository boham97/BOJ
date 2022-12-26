from collections import deque
delx = [-1, 1, 0, 0]
dely = [0, 0, 1, -1]
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
bridge = [[0] * N for _ in range(N)]
check = deque()
island = 2
ans = 10000000000000000
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            arr[i][j] = island
            island += 1
            que = deque()
            que.append([i, j])
            while que:
                x, y = que.popleft()
                for k in range(4):
                    dx = x + delx[k]
                    dy = y + dely[k]
                    if 0 <= dx < N and 0 <= dy < N and arr[dx][dy] == 1:
                        arr[dx][dy] = arr[x][y]
                        que.append([dx, dy])

for i in range(N):
    for j in range(N):
        if arr[i][j] != 0:
            x = i
            y = j
            for k in range(4):
                dx = x + delx[k]
                dy = y + dely[k]
                if 0 <= dx < N and 0 <= dy < N and arr[dx][dy] == 0:
                    check.append([x, y])
                    break


flag = 1
while check and flag:
    x, y = check.popleft()
    for k in range(4):
        dx = x + delx[k]
        dy = y + dely[k]
        if 0 <= dx < N and 0 <= dy < N:
            if arr[dx][dy] == 0:
                arr[dx][dy] = arr[x][y]
                bridge[dx][dy] = bridge[x][y] + 1
                check.append([dx, dy])
            elif arr[dx][dy] != arr[x][y]:
                if bridge[x][y]+bridge[dx][dy] < ans:
                    ans = bridge[x][y]+bridge[dx][dy]
                

                

print(ans)