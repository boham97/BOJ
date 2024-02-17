N = int(input())
K = int(input())
MAX = 1000000003
arr = [[0]*(N) for _ in range(K)]

for i in range(N):
    arr[0][i] = 1

for i in range(K - 1):
    for j in range(N):
        for k in range(j + 2, N):
            arr[i + 1][k] += arr[i][j]
        arr[i+1][j] %= MAX
    arr[i+1][N-1] = arr[i+1][N-2]

print(sum(arr[K-1])%1000000003)
