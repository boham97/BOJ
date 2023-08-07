import sys
input = sys.stdin.readline
N = 30
arr = [[0] * (N +  1) for _ in range(N)]
arr[0][0] = 1
arr[0][1] = 1
for i in range(1,N):
    arr[i][0] = 1
    for j in range(1, i + 2):
        arr[i][j] += arr[i][j-1] + arr[i-1][j]



while True:
    N = int(input())
    if N == 0:
        break

    print(arr[N-1][N])
