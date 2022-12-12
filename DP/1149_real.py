N  = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]

DP = [[0]*3 for _ in range(N)]
DP[0][0] = arr[0][0]
DP[0][1] = arr[0][1]
DP[0][2] = arr[0][2]

for i in range(N-1):
    DP[i+1][0] = min(DP[i][1],DP[i][2]) +arr[i+1][0]
    DP[i+1][1] = min(DP[i][0],DP[i][2]) +arr[i+1][1]
    DP[i+1][2] = min(DP[i][0],DP[i][1]) +arr[i+1][2]
print(min(DP[N-1]))