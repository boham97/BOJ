def dij(front):
    D = graph[front][:]
    compare = [0] * (N+1)
    compare[1] = 1
    for _ in range(N):
        w = 0
        temp = INF
        for i in range(1,N+1):
            if compare[i] == 0 and temp > D[i]:
                w = i
                temp =D[i]
        compare[w] = 1
        for i in range(1, N+1):
            D[i] = min(D[i],D[w] + graph[w][i])
    return D[must1], D[must2]

N, E = map(int,input().split())
INF = 10**9
graph = [[INF] * (N+1) for _ in range(N+1)]
for i in range(E):
    x,y,c = map(int,input().split())
    graph[x][y] = c
    graph[y][x] = c
must1, must2 = map(int,input().split())
for i in range(1+N):
    graph[i][i] = 0
temp1 = dij(1)
temp2 = dij(N)
temp3 =dij(must1)
ans = min(temp1[0]+temp2[1], temp1[1]+temp2[0])+temp3[1]
if ans < INF:
    print(ans)
else:
    print(-1)