from cmath import inf
import itertools

x, y, z = list(map(int, input().split()))

first_mat = [[] for i in range(x)]
for i in range(x):
    first_mat[i] = list(map(int,input().split()))

out_mat = [[] for i in range(x)]

turn_list = [[0,0,0] for i in range(z)]
turn_mat = [0 for i in range(z)]
for i in range(z):
    r,c,s = list(map(int, input().split()))
    turn_list[i][0] = r
    turn_list[i][1] = c
    turn_list[i][2] = s
result_mat = inf
for i in itertools.permutations(range(z),z):
    for m in range(x):
        out_mat[m] = first_mat[m][:]
    for m in i:
        #print(i,m)
        r, c, s = turn_list[m]
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
        temp2 = []
    for z1 in range(x):
        temp2.append(sum(out_mat[z1]))
    #print(min(temp2))
    if min(temp2) < result_mat:
        result_mat = min(temp2)
                #print(result_mat)
print(result_mat)    
