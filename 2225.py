N, K = map(int, input().split())

DP = [[0] * (N+1) for _ in range(K)]

DP[0] = [1] * (N+1)

for i in range(1,K):
    DP[i][0] = 1
    for j in range(1,N+1):
        DP[i][j] = (DP[i-1][j] + DP[i][j-1])%(10**9)
print(DP[-1][-1])
