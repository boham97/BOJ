from itertools import combinations
from collections import deque
def bfs(zeros):
    x,y =que[0]
    while que and zeros:
        x,y = que.popleft()
        for dx,dy in [[x+1,y],[x-1,y],[x,y+1],[x,y-1]]:
            if 0<= dx < N and 0 <= dy < N:
                if temp[dx][dy] == 0:
                    temp[dx][dy] = temp[x][y]+1
                    que.append([dx,dy])
                    zeros -= 1
                elif temp[dx][dy] == 2:
                    temp[dx][dy] = temp[x][y]+1
                    que.append([dx,dy])
                elif temp[dx][dy] != 1 and temp[dx][dy] > temp[x][y] + 1:
                    temp[dx][dy] = temp[x][y] + 1
                    que.append([dx,dy])
    temp_max = 0
    for i in range(N):
        temp_max = max(max(temp[i]),temp_max)
    #print(temp,temp_max,zeros)
    return temp_max-3, zeros

N,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
virus = deque()
zeros = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:  
            virus.append([i,j])
        if arr[i][j] == 0:
            zeros += 1
virus_num = len(virus)
mx = 10**8
for varr in combinations(range(len(virus)),M):
    temp = [arr[i][:] for i in range(N)]
    que = deque()
    for x in varr:
        que.append([virus[x][0],virus[x][1]])
        temp[virus[x][0]][virus[x][1]] = 3
    
    temper, temper2 = bfs(zeros)
    if temper2 == 0 and temper <mx:
        mx = temper
if mx == 10**8 and temper2 != 0:
    print(-1)
else:
    print(mx)
