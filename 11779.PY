import sys, heapq

input = sys.stdin.readline

N = int(input())
M = int(input())

road = [{} for _ in range(N+1)]

for _ in range(M):
    x, y, cost = map(int, input().split())
    road[x][y] = min(road[x][y], cost) if y in road[x] else cost

X, Y = map(int, input().split())

d = [1e9] * (N + 1)
route = [x] * (N + 1)

heap = []

heapq.heappush(heap,(0, X))

while heap:
    cost, node = heapq.heappop(heap)
    if d[node] < cost:
        continue
    for n, c in road[node].items():
        if d[n] > c + cost:
            d[n] = c+ cost
            heapq.heappush(heap, (c+cost, n))
            route[n] = node
            

ans = []
now = Y
while now != X:
    ans.append(now)
    now = route[now]
ans.append(X)

ans.reverse()

print(d[Y])
print(len(ans))
print(*ans)