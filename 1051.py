N, V = map(int, input().split())

arr = [input() for _ in range(N)]

num = min(N, V)
ans = 0
for s in range(num):
    for n in range(N-s):
        for v in range(V-s):
            now = arr[n][s]
            if now == arr[n+s][v] and now == arr[n][v+s] and now == arr[n+s][v+s]:
                ans = s

print((s+1)**2)
