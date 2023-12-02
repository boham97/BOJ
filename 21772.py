dx = [1, -1, 0,0]
dy = [0,0, 1, -1]
def dfs(x,y, sp, t):
    global ans
    if t == T:
        if sp > ans:
            ans = sp
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<= nx < R and 0<= ny < C and arr[nx][ny] != '#':
            if arr[nx][ny] == 'S' and visit[nx][ny] == 0:
                visit[nx][ny]  = 1
                dfs(nx, ny, sp+1, t+1)
                visit[nx][ny]  = 0
            else:
                dfs(nx, ny, sp, t+1)



ans = 0
R, C, T = map(int, input().split())
arr = list(input() for _ in range(R))
visit = [[0] * C for _ in range(R)]
for i in range(R):
    for j in range(C):
        if arr[i][j] == 'G':
            visit[i][j] = 1
            dfs(i,j,0, 0)
            break

print(ans)
