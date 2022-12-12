N, K = map(int, input().split())
coins = [0] * N
ans = [20000] * (K+1)
ans[0] = 0

for i in range(N):
    coins[i] = int(input())

for i in range(N):
    for j in range(K+1):
        if j + coins[i] <= K:
            ans[j+coins[i]] = min(ans[j+coins[i]], ans[j]+1)

if ans[-1] != 20000:
    print(ans[-1])
else:
    print(-1)
    #2294 동전2 
    