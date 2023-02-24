N = int(input())

arr = [N for _ in range(N+1)]
arr[1] = 1
for i in range(N + 1):
    if arr[i]:
        for j in (3 * i, 2 * i, i + 1):
            if j <= N and arr[j] > arr[i] + 1:
                arr[j] = arr[i] + 1

print(arr[N] - 1)
