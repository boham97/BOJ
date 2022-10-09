import sys
import heapq
V,E=map(int, sys.stdin.readline().split())
K=int(sys.stdin.readline())

dp = [1e9]*(V+1)
dp[K] = 0
graph = [[] for _ in range(V+1)]
heap = []
heapq.heappush(heap,(0,K))

for i in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((w,v))

while heap:
    cost, node = heapq.heappop(heap)
    if dp[node] < cost:
        continue
    for c, n  in graph[node]:
        if dp[n] > c+cost:
            dp[n] = c + cost
            heapq.heappush(heap,(dp[n],n))

for x in dp[1:]:
    if x != 1e9:
        print(x)
    else:
        print('INF')