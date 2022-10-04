import sys

V, E = map(int,sys.stdin.readline().split())
start = int(input())
graph = [[] for _ in range(V+1)]
for i in range(E):
    u,v,w = map(int,sys.stdin.readline().split())
    graph[u].append((v,w))
INF = 1e9
d = [INF] * (V+1)
d[start] = 0
visited = [0]*(V+1)
visited[start] = 1
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
for i in range(1,V+1):
    if d[i] == INF:
        print('INF')
    else:
        print(d[i])