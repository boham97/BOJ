n, m, h = map(int, input().split())

block = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * (1 + h) for _ in range(n + 1)]

dp[0][0] = 1

for i in range(n):
    for j in range(h + 1):
        dp[i][j] = dp[i][j] %10007
        for k in block[i]:
            if dp[i][j] and j + k <= h:
                dp[i + 1][j + k] += dp[i][j]
        dp[i + 1][j] += dp[i][j]

print(dp[-1][-1]%10007)
