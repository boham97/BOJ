t = int(input())
for _ in range(t):
    n = int(input())
    coins = list(map(int, input().split()))
    m = int(input())
    arr = [0] * (m + 1)
    arr[0] = 1
    for i in coins:
        for j in range(m+1):
            if i + j <= m:
                arr[i + j] += arr[j]
    print(arr[-1])
