import heapq
import sys

input = sys.stdin.readline

N, M, X = map(int, input().split())

road = [{} for _ in range(N+1)]
reverse = [{} for _ in range(N+1)]

for _ in range(M):
    a, b, cost = map(int, input().split())
    road[a][b] = min(road[a][b], cost) if b in road[a] else cost
    reverse[b][a] = min(reverse[b][a], cost) if a in reverse[b] else cost

heap = []
d = [1e9] * (N + 1)
dd = [1e9] * (N + 1)
heapq.heappush(heap, (0 ,X))

while heap:
    cost, node = heapq.heappop(heap)
    for next_node, next_cost in road[node].items():
        if d[next_node] > next_cost + cost:
            d[next_node] = next_cost + cost
            heapq.heappush(heap, (d[next_node], next_node))

heapq.heappush(heap, (0 ,X))
while heap:
    cost, node = heapq.heappop(heap)
    for next_node, next_cost in reverse[node].items():
        if dd[next_node] > next_cost + cost:
            dd[next_node] = next_cost + cost
            heapq.heappush(heap, (dd[next_node], next_node))


ans = 0
for i in range(1, N+1):
    if i != X and d[i] + dd[i] > ans:
        ans = d[i] + dd[i]


print(ans)