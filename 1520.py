
dlt = [[-1,0],[0,1], [0, -1],[1,0]]
N, M = map(int,input().split())
cnt = 0
arr = [list(map(int, input().split())) for _ in range(N)]
DP = [[0] * M for _ in range(N)]
DP[0][0] = 1
visited = [[[0]*M for _ in range(N)]]
visited[0][0] = 1
stack = [[0,0,-1]]
nodrt = -1
while stack:
    x, y,drt = stack[-1]
    if x== N-1 and y==M-1:
        cnt += 1
        print(stack)
        for x,y,z in stack:
            DP[x][y] = 1
    for i in range(4):
        dx, dy = x+dlt[i][0], y+dlt[i][1]
        if 0<= dx < N and 0<= dy < M and arr[x][y] > arr[dx][dy] and i != nodrt:
            if DP[dx][dy] == 0 and visited[dx][dy] == 0:
                visited[dx][dy] = 1
                stack.append([dx,dy,i])
                nodrt = -1
                break
            elif DP[dx][dy] != 0 and visited[dx][dy]== 1:
                for x,y,z in stack:
                    DP[x][y] += DP[dx][dy] 
                print(stack)
                print(nodrt, i)
                cnt += DP[dx][dy]
                DP[dx][dy] +=1
            
    else:
        buffer1, buffer2, nodrt = stack.pop()
print(DP)
print(visited)
print(cnt)