import sys
N = int(input())
arr = list(map(int,sys.stdin.readline().split()))
DP = [[0]*(N+1) for _ in range(4)]
for i in range(1,N+1):
    if arr[i+1] > DP[1][i]:
        DP[1][i+1] = arr[i+1]
        DP[0][i+1] = DP[0][i] + 1
    if arr[i+1] > DP[3][i]:
        DP[1][i+1] = arr[i+1]
        DP[0][i+1] = DP[3][i] + 1
    