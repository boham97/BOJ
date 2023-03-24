N, L = map(int , input().split())

arr = list( list(map(int, input().split())) for _ in range(N))

arr.sort()
ans = 0
mid = -L

for start, end in arr:
    start = max(start, mid)
    temp = (end - start) // L
    if (end - start) % L:
        temp += 1
    ans += temp
    mid = start + temp * L

print(ans)
        
