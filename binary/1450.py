n, c = map(int, input().split())
arr = list(map(int,input().split()))

res1, res2 = [],[]
a, b = n//2, n//2
if n%2:
    b += 1
for i in range(1<<(a)):
    j = i
    w = 0
    index = 0
    while j:
        if j%2:
            w += arr[index]
        index += 1
        j = j//2
    res1.append(w)

for i in range(1<<(b)):
    j = i
    w = 0
    index = 0
    while j:
        if j%2:
            w += arr[index + a]
        index += 1
        j = j//2
    res2.append(w)


def right(target, arr):
    l, r = 0, len(arr) -1
    while l <= r:
        m = (l + r)// 2
        if arr[m] > target:
            r = m - 1
        else:
            l = m + 1
    return r

res1.sort()
res2.sort()
ans = 0

for i in res1:
    ans += right(c - i, res2) + 1

print(ans)
