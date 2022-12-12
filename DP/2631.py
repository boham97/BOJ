N = int(input())
arr = []
for i in range(N):
    arr.append(int(input()))

DP = [[0]* (1+N) for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(1,N+1):
        if arr[i-1] == j:
            DP[i][j] = DP[i-1][j-1] +1
        else:
            DP[i][j] = max(DP[i][j-1],DP[i-1][j])

print(N-max(DP[-1]))
