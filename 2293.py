N, K = map(int, input().split())
coins = [0] * N
ans = [0] * (K+1)
ans[0] = 1

for i in range(N):
    coins[i] = int(input())

for i in range(N):
    for j in range(K+1):
        if j + coins[i] <= K:
            ans[j+coins[i]] += ans[j]

print(ans[-1])