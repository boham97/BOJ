n, m = map(int, input().split())
inf = 1e10
distance = [inf] * (n + 1)
distance[1] = 0
edge = []
for _ in range(m):
    edge.append(list(map(int, input().split())))


for i in range(1, n):
    for j in range(m):
        now, next, cost = edge[j]
        if distance[now] != inf and distance[next] > distance[now] + cost:
            distance[next] = distance[now] + cost

for j in range(m):
    now, next, cost = edge[j]
    if distance[now] != inf and distance[next] > distance[now] + cost:
        print(-1)
        break
else:
    for i in range(2, n + 1):
        print(distance[i] if distance[i] != inf else -1)
