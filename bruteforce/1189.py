r, c, k = map(int,input().split())
arr = list(list(input()) for _ in range(r))
arr[r-1][0] = 'T'
delta = [[1,0], [-1, 0], [0,1], [0,-1]]
ans = [0]
def dfs(x, y, cnt):
    if cnt == k - 1 and x == 0 and y == c - 1:
        ans[0] += 1
        return
    for i in range(4):
        dx = x + delta[i][0]
        dy = y + delta[i][1]
        if 0 <= dx < r and 0 <= dy < c and arr[dx][dy] != 'T':
            arr[dx][dy] = 'T'
            dfs(dx, dy, cnt + 1)
            arr[dx][dy] = '.'


dfs(r-1, 0, 0)
print(*ans)
