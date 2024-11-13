from heapq import heappush, heappop
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
inf = 1e10
h = []
distance = [[inf] * n for _ in range(2)]
distance
sub = [0] * n
for i in range(n):
    sub[i] = int(input())
    
arr = [[] for _ in range(n)]
for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(n):
        if temp[j] == 0: continue
        arr[i].append((j, temp[j]))

distance[0][0] = 0
distance[1][0] = 0
heappush(h, (0, 0, 0))

while h:
    change, cost, now = heappop(h)
    for node, edge in arr[now]:
        next_change = change
        if sub[now] != sub[node]: next_change += 1
        if next_change < distance[0][node]:
            heappush(h, (next_change, cost + edge, node))
            distance[0][node] = next_change
            distance[1][node] = cost + edge
        elif next_change == distance[0][node] and cost + edge < distance[1][node]:
            heappush(h, (next_change, cost + edge, node))
            distance[0][node] = next_change
            distance[1][node] = cost + edge

print(distance[0][m], distance[1][m])
