n,m = map(int, input().split())
arr = list(input() for _ in range(n))
visit = [[0] * m for _ in range(n)]
dp = [[0] * m for _ in range(n)]
ans = [[0] * m for _ in range(n)]
delta = [-1, 1, 0, 0]
stack = []
visit[0][0] = 1
def dfs(turn, x, y):
    global ans
    now = int(arr[x][y])
    for i in range(4):
        dx = x + delta[i] * now
        dy = y + delta[3-i] * now
        if 0 <= dx < n and 0 <= dy < m and arr[dx][dy] != 'H' :
            if dp[dx][dy] == 1:
                continue
            if visit[dx][dy]:
                print(-1)
                exit()
            visit[x][y] = 1
            dfs(turn +1, dx, dy)
            visit[dx][dy] = 0
    dp[x][y] = 1
    stack.append((x,y))
        
dfs(1,0,0)

res = 0
while stack:
    x,y = stack.pop()
    now = int(arr[x][y])
    for i in range(4):
        dx = x + delta[i] * now
        dy = y + delta[3-i] * now
        if 0 <= dx < n and 0 <= dy < m and arr[dx][dy] != 'H' and ans[dx][dy] < ans[x][y] + 1:
            ans[dx][dy] = ans[x][y] + 1
            res = max(res, ans[dx][dy])
                      
print(res + 1)
        
