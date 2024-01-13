dp = [0] * 10001
dp[1] = 1
dp[2] = 2
dp[3] = 3
for i in range(4,10001):
    dp[i] = dp[i-3] + i//2 + 1

t = int(input())
for _ in range(t):
    n = int(input())
    print(dp[n])
