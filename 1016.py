n, m = map(int, input().split())

arr = [0] * (m - n + 1)
for i in range(2, int(m**0.5) + 1):
        j = n// i** 2
        while i ** 2 * j <= m:
            if i ** 2 * j >= n and arr[i ** 2 * j - n] == 0:
                arr[i ** 2 * j - n] = 1
            
            j += 1
print(m-n-sum(arr) + 1)
