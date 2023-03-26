n, m, r = map(int, input().split())

item = list(map(int, input().split()))

route = list([20] * (n+1) for _ in range(n+1))

for i in range(n+1):
    route[i][i] = 0

for _ in range(r):
    a, b, l = map(int, input().split())
    route[a][b] = l
    route[b][a] = l

# j -> k 갈때 i를 무조건 거쳐서 확인해본다
for i in range(1,n+1):
    for j in range(1,n+1):
        if route[i][j] <= m:
            for k in range(1, n+1):
                route[j][k] = min(route[j][k], route[j][i] + route[i][k])

ans = 0

for i in range(1,n+1):
    temp = 0
    for j in range(1,n+1):
        if route[i][j] <= m:
            temp += item[j - 1]
    if temp > ans:
        ans = temp

print(ans)