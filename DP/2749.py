def fibo(n):
    if n in dp:
        return dp[n]
    if n%2:
        temp = (fibo(n//2 + 1) ** 2 + fibo(n//2) ** 2)%1000000
    else:
        temp = (fibo(n//2 + 1) ** 2 - fibo(n//2 - 1) ** 2)%1000000
    dp[n] = temp
    return temp
dp = {}
dp[0] = 0
dp[1] = 1
dp[2] = 1
ans = fibo(int(input()))
print(ans)

