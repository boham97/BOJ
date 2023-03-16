N = int(input())

arr = [0] * (N + 1)

for i in range(1,N+1):
    arr[i] = i

for i in range(1, N+1):
    for j in range(1, int(i**0.5 + 1)):
        if arr[i] > arr[i- j * j] + 1:
            arr[i] = arr[i- j * j] + 1
print(arr[N])