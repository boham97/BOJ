def bfs(attempt,temp):
    global ans
    arr =list(range(N))
    for i in range(1,N):
        num = i
        for j in range(1,H):
            if graph[j][num] == 1:
                num +=1
            elif graph[j][num-1] == 1:
                num -= 1
        if i != num:
            break
    else:
        if ans > attempt or ans == -1:
            ans = attempt
        
    if attempt == 3:
        return
    for i in range(1,H):
        for j in range(1,N-1):
            if graph[i][j] != 1 and graph[i][j-1] != 1 and graph[i][j] != 1 and (j+1 == N or graph[i][j+1] == 0) and N*i +j >N*temp[-1][0]+temp[-1][1]:
                graph[i][j] = 1
                bfs(attempt + 1,temp+[[i,j]])
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
bfs(0,[[0,0]])
print(ans)