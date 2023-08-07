N = int(input())

arr = [[0] * 10 for _ in range(N)]

for i in range(1,10):
    arr[0][i] = 1

for i in range(N-1):
    for j in range(10):
        if j > 0:
            arr[i + 1][j - 1] += arr[i][j]
            arr[i + 1][j - 1] %= 1000000000
        if j < 9:
            arr[i + 1][j + 1] += arr[i][j]
            arr[i + 1][j + 1] %= 1000000000
    
print(sum(arr[N-1])%1000000000)
