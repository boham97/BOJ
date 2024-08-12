N, C = map(int, input().split())
M = int(input())
arr = []
for _ in range(M):
    arr.append(list(map(int, input().split())))
arr.sort()

dp = [0] * (N + 1)
weight = 0
ans = 0
for i in range(M):
    a, b, c = arr[i]
    dp[b] += c
    weight += c
    for k in range(a + 1):
        if dp[k]:
            ans += dp[k]
            weight -= dp[k]
            dp[k] = 0
    j = N
    while weight > C:
        if dp[j]:
            dump = dp[j] if weight - dp[j] >= C else weight -C
            weight -= dump
            dp[j] -= dump
        j -= 1


print(ans + sum(dp))
    