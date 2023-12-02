n = int(input())
dp = [0] * 1000001
dp[1] = 1
dp[2] = 2
dp[3] = 3
for i in range(4, n + 1):
    temp = i
    for j in range(int( i ** 0.5) + 2):
        if temp < dp[j]*dp[i - j]:
            temp = dp[j]*dp[i - j]
    dp[i] = temp

print(dp[n]%10007)
