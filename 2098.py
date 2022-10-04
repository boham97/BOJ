from pprint import pprint
import random

def dfs(i,cost):
    global ans
    if cost >= ans:
        return
    if i == N:
        cost = cost + matrix[mat[i-1]][mat[0]] - minmin[mat[i-1]]
        #print(mat,cost)
        if cost < ans:
            ans = cost
        return
    else:
        for j in range(i,N):
            mat[i], mat[j] = mat[j], mat[i]
            dfs(i+1, cost + matrix[mat[i-1]][mat[i]]-minmin[mat[i-1]])
            mat[i], mat[j] = mat[j], mat[i]

N = int(input())
matrix = [list(map(int,input().split())) for _ in range(N)]
minmin = [0] * N
INF = 10**9
ans = INF
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 0:
            matrix[i][j] = INF
minsum = 0
for i in range(N):
    minmin[i] = min(matrix[i])
    minsum += minmin[i]
#pprint(matrix)
mat = list(range(N))
random.shuffle(mat)
dfs(1,minsum)
print(ans)