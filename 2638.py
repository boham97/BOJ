import sys
from collections import deque
import heapq
from pprint import pprint

delx = [-1, 1, 0, 0]
dely = [0, 0 ,1, -1]


input = sys.stdin.readline

N, M = map(int, input().split())

arr = list(list(map(int,input().split())) for _ in range(N))



air = deque()
air.append((0,0))
arr[0][0] = 2

while air:
    x, y = air.popleft()
    

    for i in range(4):
        dx = x + delx[i]
        dy = y + dely[i]
        if 0 <= dx < N and 0 <= dy < M:
            if arr[dx][dy] == 0:
                air.appendleft((dx,dy))
                arr[dx][dy] = arr[x][y]
            elif arr[dx][dy] == 1:
                logic = 0
                for i in range(4):
                    dx2 = dx + delx[i]
                    dy2 = dy + dely[i]
                    if 0 <= dx2 < N and 0 <= dy2 < M and 1< arr[dx2][dy2] <= arr[x][y]:
                        logic += 1
                if logic > 1:
                    arr[dx][dy] = arr[x][y] + 1
                    air.append((dx,dy))


ans = 0
for i in range(N):
    ans = max(max(arr[i]), ans)

print(ans-2)