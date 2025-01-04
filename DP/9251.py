a = input().rstrip()
b = input().rstrip()

dp = [[0] * (1 + len(a)) for _ in range(len(b) + 1)]

for i in range(len(b)):
    for j in range(len(a)):
        dp[i + 1][j + 1] = max(dp[i][j] + 1 if b[i]==a[j] else 0, dp[i + 1][j], dp[i][j + 1])


print(dp[-1][-1])
