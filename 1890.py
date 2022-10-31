N = int(input())
arr = [list(map(int, input().split())) for _ in range(4)]
DP = [[0]* N for _ in range(4)]
DP[0][0] = 1
for i in range(N):
    for j in range(N):
        if i == N-1 and j == N-1:
            continue
        if i+arr[i][j] <N:
            DP[i+arr[i][j]][j] += DP[i][j]
        if j+arr[i][j] <N:
            DP[i][j+arr[i][j]] += DP[i][j]
    
print(DP[-1][-1])