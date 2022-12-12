N = int(input())
arr = [[0,0] for _ in range(N)]
for i in range(N):
    x, y = map(int, input().split())
    arr[i][0], arr[i][1] = x, y
arr.sort()
DP = [[0] * (501) for _ in range(N+1)]
for i in range(1,N+1):
    for j in range(1,501):
        if arr[i-1][1] == j:
            DP[i][j] = DP[i-1][j-1] +1
        else:
            DP[i][j] = max(DP[i][j-1],DP[i-1][j])

print(N -max(DP[-1]))
