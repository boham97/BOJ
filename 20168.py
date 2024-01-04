from heapq import heappush, heappop
inf = 123456789
n, m, a, b, c = map(int, input().split())
distance = [inf] * (1 + n)
distance[a] = 0
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y,z))
    graph[y].append((x,z))

hq = []
heappush(hq,(0, 0, a))

while hq:
    mind, cost, now = heappop(hq)
    for x, z in graph[now]:
        if max(mind, z) < distance[x] and cost + z <= c:
            distance[x] = max(mind, z) 
            heappush(hq, (distance[x], cost + z, x))
            
print(distance[b] if distance[b] < inf else -1)
