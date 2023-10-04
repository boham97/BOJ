n = int(input())

arr = list(map(int, input().split()))
p = int(input())

dp = [0] * (p+1)
for i in range(n):
    if arr[i] <= p:
        dp[arr[i]] = i
for i in range(p + 1):
    for j in range(n):
        if i + arr[j] < p + 1:
            num = dp[i]
            grid = 0
            size = 0
            temp = 0
            while num:
                temp = num % 10
                if temp < j:
                    grid = grid + temp * 10 ** size
                    num  = num // 10
                else:
                    num = num * 10 + j
                    break
                size += 1
            dp[i + arr[j]] = max ( dp[i + arr[j]] , grid + (num) * 10 ** size)
print(max(dp))
