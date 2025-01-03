n = int(input())

arr = [[0] * 3 for _ in range(n + 1)]
wine = [0] * n
for i in range(n):
    wine[i] = int(input())

for i in range(n):
    arr[i + 1][1] = max(arr[i][1], arr[i][0] + wine[i])
    arr[i + 1][2] = max(arr[i][2], arr[i][1] + wine[i])
    arr[i + 1][0] = max(arr[i][0], arr[i][1], arr[i][2])

print(max(arr[n]))
