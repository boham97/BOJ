C, N = map(int, input().split())

arr =  [1e9] * (C + 1)
arr[0] = 0

for i in range(1,N+1):
    c, n = map(int, input().split())
    for j in range(C):
        if j+n <= C and arr[j+n] > arr[j] + c:
            arr[j+n] = arr[j] + c
        elif j+n > C and arr[C] > arr[j] + c:
            arr[C] = arr[j] + c
print(arr[-1])
