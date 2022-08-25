def bfs(attempt):
    global ans
    arr =list(range(N))
    for x in range(H):
        for y in range(N):
            if graph[x][y] == 1:
                arr[y], arr[y+1] = arr[y+1], arr[y]
    if arr == list(range(N)):
        ans = attempt
        return
    elif attempt == 3:
        return
    for i in range(1,H):
        for j in range(1,N-1):
            if graph[i][j] == 0 and graph[i][j-1] == 0 and graph[i][j] == 0 and (j+1 == N or graph[i][j+1] == 0):
                graph[i][j] = 1
                bfs(attempt + 1)
                graph[i][j] = 0
        

N, M, H = map(int,input().split())
N += 1
H += 1
graph = [[0]*N for _ in range(H)]
arr = list(range(N))
for i in range(M):
    x, y = map(int,input().split())
    graph[x][y] = 1

ans = -1
bfs(0)
print(ans)