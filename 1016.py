n, m = map(int, input().split())

arr = [0] * (m - n + 1)
for i in range(2, 1001001):
    if arr[i] == 0:
        j = 1
        while i ** 2 * j <= m:
            arr[i ** 2 * j] = 1
            j += 1
print(m-n-sum(arr[n:m+1])+1)