n, m = map(int, input().split())
graph = [[10000000] * (n + 1) for _ in range(n + 1)]
ans = [[0] * (n + 1) for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c
    graph[b][a] = c
    ans[a][b] = b
    ans[b][a] = a

for i in range(n + 1):
    graph[i][i] = 0
    for j in range(n+ 1):
        for k in range(n+ 1):
            if graph[j][k] > graph[j][i] + graph[i][k]:
                graph[j][k] = graph[j][i] + graph[i][k]
                ans[j][k] = ans[j][i]

for i in range(1, n+1):
    ans[i][i] = "-"
    print(*ans[i][1::])
