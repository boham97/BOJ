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
for i in range(1,V+1):
    if d[i] == INF:
        print('INF')
    else:
        print(d[i])
print(graph)