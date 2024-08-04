n, m = map(int, input().split())
k = int(input())
road = [[[0] * (m + 1) for _ in range(n + 1)] for _ in range(2)]

for _ in range(k):
    a, b, c, d = map(int, input().split())
    if a != c:
        if c < a:
            a, b, c, d = c, d, a, b
        road[1][a][b] = 1
    else:
        if b > d:
            a, b, c, d = c, d, a, b
        road[0][a][b] = 1

dp = [[0] * (m + 1) for _ in range(n + 1)]
dp[0][0] = 1
for i in range(n + 1):
    for j in range(m + 1):
        if  j + 1 <= m and road[0][i][j] == 0:
            dp[i][j + 1] += dp[i][j]
        if  i + 1 <= n and road[1][i][j] == 0:
            dp[i + 1][j] += dp[i][j]

print(dp[-1][-1])