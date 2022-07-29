
n = int(input())

mat = [[] for i in range(n)]
result_mat = [[[0,0,0,] for j in range(n)] for i in range(n)]
for i in range(n):
    mat[i]= list(map(int,input().split()))
result_mat[0][1][0] =1
for i in range(2,n):
    if mat[0][i-1] ==0 and mat[0][i] == 0:
        result_mat[0][i][0] = result_mat[0][i-1][0]
for i in range(1,n):
    for j in range(2,n):
        if mat[i][j-1] == 0 and mat[i][j] ==0:
            result_mat[i][j][0] = result_mat[i][j][0] + result_mat[i][j-1][0] + result_mat[i][j-1][2]
        if mat[i][j-1] ==0 and mat[i][j] ==0 and mat[i-1][j] == 0:
            result_mat[i][j][2] = result_mat[i][j][2] + result_mat[i-1][j-1][0] +result_mat[i-1][j-1][1] + result_mat[i-1][j-1][2]
        if mat[i-1][j] == 0 and mat[i][j] == 0:
            result_mat[i][j][1] =result_mat[i][j][1] + result_mat[i-1][j][2] + result_mat[i-1][j][1]



print(sum(result_mat[n-1][n-1]))