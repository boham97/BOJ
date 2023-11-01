dp = [ i for i in range(100)]
for i in range(100):
    if i + 10 < 100:
        dp[i+10] = min(dp[i+10], dp[i] + 1)
    if i + 25 < 100:
        dp[i+25] = min(dp[i+25], dp[i] + 1)

t = int(input())
for _ in range(t):
    n = int(input())
    ans = 0
    while n:
        now = n%100
        ans += dp[now]
        n = n//100
    print(ans)
