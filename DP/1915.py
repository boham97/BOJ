n,m = map(int, input().split())
arr = list(list(map(int, input())) for _ in range(n))
ans = 0
dp = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if arr[i][j]:
            dp[i][j] = 1

for i in range(1, n):
    for j in range(1, m):
        if dp[i][j]:
            dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1

for i in range(n):
    ans = max(ans, max(dp[i]))
print(ans **2)
