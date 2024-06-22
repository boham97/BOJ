import sys


N = int(input())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dp = [[0]*(N) for _ in range(N)]

for i in range(1, N):
    for j in range(N):
        if j + i == N:
            break

        dp[j][j+ i] = int(1e9)

        for k in range(j, j + i):
            dp[j][i + j] = min(dp[j][i + j],
                               dp[j][k] + 
                               dp[k+1][i+ j] + 
                                        arr[j][0] * arr[k][1] * arr[i+ j][1])

print(dp[0][-1])
