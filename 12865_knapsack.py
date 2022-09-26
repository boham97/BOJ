N, K = map(int,input().split())
cost = [[0] * (K+1) for _ in range(N+1)]
for i in range(N):
    w, v = map(int,input().split())
    for j in range(K+1):
        if w > j:
            cost[i+1][j] = cost[i][j]
        if j + w < K+1:
            cost[i+1][j+w] = max(cost[i][j] + v, cost[i][j+w])

print(cost[N][K])

'''
6 304
98 98
4 4
6 6
100 100
101 101
103 103
'''
