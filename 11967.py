from collections import deque

N, M = map(int, input().split())
arr = list([0] * (N + 1) for _ in range(N + 1))
arr[0][0] = 1
connect1 = list(list(list() for _ in range(N+1)) for _ in range(N+1))
connect2 = list(list(list() for _ in range(N+1)) for _ in range(N+1))


for _ in range(M):
    x, y,x2, y2 = map(int, input().split())
    connect1[x][y].append(x2)
    connect2[x][y].append(y2)

print(connect1)
print(connect2)
