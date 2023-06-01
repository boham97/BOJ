import sys

ans = 0

N = int(sys.stdin.readline())

arr = list( list(map(int, sys.stdin.readline().split())) for _ in range(N))

arr.sort()

last = arr[0][0]
for i, j in arr:
    if j <= last:
        continue
    else:
        ans += (j - max(last, i))
        if j > last:
            last = j     

print(ans)
