def dfs(i,cost):
    global ans
    temp = cost
    for j in range(i+1,N):
        temp += minmin[mat[j]]
    if temp+ minmin[0] > ans:
        return
    if i == N:
        cost += matrix[mat[i-1]][0]
        if cost < ans:
            ans = cost
        return
    else:
        for j in range(i,N):
            mat[i], mat[j] = mat[j], mat[i]
            if matrix[mat[i-1]][mat[i]] == 0:
                pass
            dfs(i+1, cost + matrix[mat[i-1]][mat[i]])
            mat[i], mat[j] = mat[j], mat[i]

N = int(input())
matrix = [list(map(int,input().split())) for _ in range(N)]
minmin = [0] * N
ans = 1000000 * N
minsum = 0
for i in range(N):
    minmin[i] = min(matrix[i])
    minsum += minmin[i]
mat = list(range(N))
dfs(1,0)
print(ans)