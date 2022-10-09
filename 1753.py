import sys
import heapq
V,E=map(int, sys.stdin.readline().split())
K=int(sys.stdin.readline())

dp = [1e9]*(V+1)
dp[K] = 0
graph = [[] for _ in range(V+1)]
<<<<<<< HEAD
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
=======
for i in range(E):
    u,v,w = map(int,sys.stdin.readline().split())
    graph[u].append((v,w))
INF = 1e9
d = [INF] * (V+1)
d[start] = 0
visited = [0]*(V+1)
visited[start] = 1
<<<<<<< HEAD
for j,k in graph[start]:
    d[j] = min(d[j],k)
for i in range(1,V+1):
    graph[i].sort(key = lambda x:x[1],reverse=True)
for _ in range(V):
    temp_min = INF
    next = 0
    for i in range(V):
        if visited[i] == 1:
            continue
        for j in range(len(graph[i])-1,-1,-1):
            if visited[graph[i][j][0]] == 0 and graph[i][j][1]<temp_min:
                temp_min = graph[i][j][1]
                next = graph[i][j][0]
    visited[next] = 1
    for i in range(len(graph[next])):
        d[graph[next][i][0]] = min(d[graph[next][i][0]], d[next]+graph[next][i][1])
=======
used =[start]
for j,k in graph[start]:
    d[j] = min(d[j],k)

for _ in range(V):
    temp_min = INF
    next = 0
    for i in used:
        for j,k in graph[i]:
            if visited[j] == 0 and k<temp_min:
                temp_min = k
                next = j
    visited[next] = 1
    used.append(next)
    for i,j in graph[next]:
        d[i] = min(d[i], d[next]+j)
    #print(d)
>>>>>>> 9ab4d46fca30cf41210c3fefd9a626b9f9d66caf
for i in range(1,V+1):
    if d[i] == INF:
        print('INF')
    else:
<<<<<<< HEAD
        print(d[i])
print(graph)
=======
        print(d[i])
>>>>>>> 9ab4d46fca30cf41210c3fefd9a626b9f9d66caf
>>>>>>> ba140444107e26e3fa75a12b44a4e8e936c7c0ee
