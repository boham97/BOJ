import sys

input = sys.stdin.readline

t = int(input())


for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    i, j = 0, n -1
    temp = 9999999999
    cnt = 0

    while(i < j):
        if abs(arr[i] + arr[j] - k) < temp:
            temp = abs(arr[i] + arr[j] - k)
            cnt = 1
        elif abs(arr[i] + arr[j] - k) ==  temp:
            cnt += 1
        else:
            pass

        if arr[i] + arr[j] >= k:
            j -= 1
        else:
            i += 1

    print(cnt)
