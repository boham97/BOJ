from collections import deque

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
size = 2
ate = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == 9:
            temp = [i,j]
arr[temp[0]][temp[1]] = 0
time = 0
que = deque()
que.append(temp)

target = [[0,0]]
while target:
    target = []
    visited = [[N*N+1]*N for _ in range(N)]
    visited[que[0][0]][que[0][1]]  = 0
    while que:
        x, y = que.popleft()
        for dx,dy in [[x-1,y],[x+1,y],[x,y+1],[x,y-1]]:
            if 0<= dx<N and 0<=dy<N and arr[dx][dy] <= size and visited[dx][dy] > visited[x][y] +1:
                que.append([dx,dy])
                visited[dx][dy] = visited[x][y] +1
                if 0 < arr[dx][dy] < size:
                    target.append([visited[x][y] +1, dx,dy])
    #print(visited)
    #print(target)
    if len(target) == 0:
        break
    target.sort()
    time += target[0][0]
    que.append([target[0][1],target[0][2]])
    arr[target[0][1]][target[0][2]] = 0
    ate += 1
    if ate == size:
        size += 1
        ate = 0

print(time)

