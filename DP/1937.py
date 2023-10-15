dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x,y):
    if visit[x][y] != 0:
        return visit[x][y]

    depth = 0;
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<= nx < n and 0 <= ny < n and arr[x][y] < arr[nx][ny]:
            depth = max(depth, dfs(nx,ny))
    visit[x][y] = depth + 1
    return depth + 1
            

n = int(input())
arr = list(list(map(int, input().split())) for _ in range(n))
visit = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        dfs(i,j)
ans = 0
for i in range(n):
    ans = max(ans, max(visit[i]))
print(ans)
