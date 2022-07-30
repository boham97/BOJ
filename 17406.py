from cmath import inf


x, y, z = list(map(int, input().split()))

first_mat = [[] for i in range(x)]
for i in range(x):
    first_mat[i] = list(map(int,input().split()))

out_mat = [[] for i in range(x)]
for i in range(x):
    out_mat[i] = first_mat[i][:]
for i in range(z):
    r, c, s = list(map(int, input().split()))
    for j in range(1, s + 1):
        temp =out_mat[r -j -1][c -j -1]
        for k in range(2*j):
            out_mat[r-j-1+k][c-j-1] = out_mat[r-j-1+k+1][c-j-1]
        for k in range(2*j):
            out_mat[r+j-1][c-j-1+k] = out_mat[r+j-1][c-j-1+k+1]
        for k in range(2*j):
            out_mat[r+j-1-k][c+j-1] = out_mat[r+j-1-k -1][c+j-1]
        for k in range(2*j):
            out_mat[r-j-1][c+j-1-k] = out_mat[r-j-1][c+j-1-k-1]
        out_mat[r-j-1][c-j] = temp
result_mat = inf
for i in range(x):
    temp2 =sum(out_mat[i])
    if temp2 < result_mat:
        result_mat = temp2
print(result_mat)
    
