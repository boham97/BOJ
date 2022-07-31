from cmath import inf
import itertools

x, y, z = list(map(int, input().split()))

first_mat = [[] for i in range(x)]
for i in range(x):
    first_mat[i] = list(map(int,input().split()))

out_mat = [[] for i in range(x)]
for i in range(x):
    out_mat[i] = first_mat[i][:]

turn_list = [[0,0,0] for i in range(z)]
turn_mat = [0 for i in range(z)]
for i in range(z):
    r,c,s = list(map(int, input().split()))
    turn_list[i][0] = r
    turn_list[i][1] = c
    turn_list[i][2] = s
result_mat = inf
for i in itertools.permutations(turn_list,z):
    for n in range(z+1):
        #print(i,n)
        for p in list(itertools.combinations(i,n)):
            for m in range(x):
                out_mat[m] = first_mat[m][:]
            for m in i:
                #print(i,n,p,m)
                if m not in p:
                    r, c, s = m
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
                else:
                    r, c, s = m
                    for j in range(1, s + 1):
                        temp =out_mat[r -j -1][c -j -1]
                        for k in range(2*j):
                            out_mat[r-j-1][c-j-1+k] = out_mat[r-j-1][c-j-1+k+1]
                        for k in range(2*j):
                            out_mat[r-j-1+k][c+j-1] = out_mat[r-j-1+k+1][c+j-1]
                        for k in range(2*j):
                            out_mat[r+j-1][c+j-1-k] = out_mat[r+j-1][c+j-1-k-1]
                        for k in range(2*j):
                            out_mat[r+j-1-k][c-j-1] = out_mat[r+j-1-k-1][c-j-1]
                    out_mat[r-j-1][c-j] = temp
            for z in range(x):
                temp2 =sum(out_mat[z])
            if temp2 < result_mat:
                result_mat = temp2
                #print(result_mat)
print(result_mat)    
