N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
DP = [[0] * i for i in range(1,N+1)]
DP[0][0] = arr[0][0]

for i in range(1,N):
    for j in range(i+1):
        if j == 0:
            DP[i][j] = DP[i-1][0] + arr[i][j]
        elif j == i:
            DP[i][j] = DP[i-1][i-1] + arr[i][j]
        else:
            DP[i][j] = max(DP[i-1][j-1],DP[i-1][j]) + arr[i][j]
print(max(DP[N-1]))