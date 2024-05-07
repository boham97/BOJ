from collections import deque

n, m, k = map(int, input().split())
arr = list( input().rstrip() for _ in range(n))
word = input().rstrip()


dp = [[[0] * len(word) for _ in range(m)] for _ in range(n)]
que = deque()
ans = 0
size = len(word) - 1
for i in range(n):
    for j in range(m):
        if arr[i][j] == word[0]:
            que.append((i, j, 0))
            dp[i][j][0] = 1
delta = [[-1, 1, 0,0], [0, 0, 1, -1]]
while que:
    x, y, t = que.popleft()
    if t == size:
        ans += dp[x][y][t]
        continue
    for i in range(4):
        dx, dy = x, y
        for j in range(k):
            dx += delta[0][i]
            dy += delta[1][i]
            if 0 <= dx < n and 0 <= dy < m and arr[dx][dy] == word[t + 1]:
                if dp[dx][dy][t+1] == 0:
                    que.append((dx,dy, t+1))
                dp[dx][dy][t+1] += dp[x][y][t]
print(ans)
