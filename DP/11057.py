N = int(input())

arr = [[0] * 10 for i in range(N)]
arr[0] = [1] * 10
for i in range(1,N):
    for j in range(10):
        for k in range(j+1):
            arr[i][j] += arr[i-1][k]
        arr[i][j] %= 10007

print(sum(arr[N-1])%10007)
