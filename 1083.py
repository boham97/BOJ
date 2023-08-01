N = int(input())
arr = list(map(int, input().split()))
s = int(input())

target = 0
coin = s
while (coin > 0 and target < N):
    temp = arr[target]
    index = target
    for i in range(target + 1, min(N, target +coin + 1)):
        if arr[i] > temp:
            temp = arr[i]
            index = i
    if temp > arr[target]:
        for i in range(index, target, -1):
            arr[i] = arr[i - 1]
        arr[target] = temp
        coin -= index - target

    target += 1
print(*arr)
