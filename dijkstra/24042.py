from heapq import heappop, heappush
import sys
input = sys.stdin.readline
inf  = 1e12

n,m = map(int, input().split())
distance = [inf] * (1+n)
distance[1] = 0
arr = [[] for _ in range(n+1)]
hq = []
heappush(hq, (0, 1))
for i in range(1, m + 1):
    a, b = map(int, input().split())
    arr[a].append((b, i))
    arr[b].append((a, i))

while hq:
    current_distance, now = heappop(hq)
    if distance[now] < current_distance:
        continue
    if current_distance >distance[n]:
        break
    for next_node, cost in arr[now]:
        
        new_cost = cost - current_distance % m
        new_cost += m if new_cost < 0 else 0
        new_distance = new_cost + current_distance
        if distance[next_node] > new_distance:
            distance[next_node] = new_distance
            heappush(hq, (new_distance, next_node))
                     
print(distance[n])
