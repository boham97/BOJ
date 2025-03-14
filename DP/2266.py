n, m = map(int, input().split())

dp = [[0] * (n + 1) for _ in range(m + 1)]
for i in range(n + 1):
    dp[1][i] = i
for i in range(2, m + 1):
    for j in range(n + 1):
        if j <i:
            dp[i][j] = dp[i -1][j]
            continue
        temp = 500
        for k in range(j//2 + 1):
            #print(i, j, k, j -k -1, max(dp[i -1][k], dp[i][j -k - 1]))
            temp = min(temp , max(dp[i -1][k], dp[i][j -k - 1]))
        dp[i][j] = temp + 1

print(dp[-1][-1])
