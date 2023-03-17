N = int(input())
temp = 1000000007
arr = [[0] * (N + 1) for _ in range(3)]

arr[2][1] = 1


for i in range(1,N):
    arr[0][i+1] = (arr[2][i] + arr[1][i])%temp
    arr[1][i+1] = (arr[2][i] + arr[0][i])%temp
    arr[2][i+1] = (arr[0][i] + arr[1][i])%temp

print(arr[0][N])
