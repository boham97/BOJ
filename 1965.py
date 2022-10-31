N = int(input())
arr = list(map(int, input().split()))

DP = [[0] * (1001) for _ in range(N+1)]
for i in range(1,N+1):
    for j in range(1,1001):
        if arr[i-1] == j:
            DP[i][j] = DP[i-1][j-1] +1
        else:
            DP[i][j] = max(DP[i][j-1],DP[i-1][j])

print(max(DP[-1]))
