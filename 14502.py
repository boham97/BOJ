N, M = map(int,input().split())
arr = [[] for _ in range(N)]
mat = [[] for _ in range(N)]

for i in range(N):
    arr[i] = list(map(int,input().split()))
    mat[i] = arr[i][:]


result_max = 0
for i in range(N*M-2):
    if arr[i//M][i%M] == 1 or  arr[i//M][i%M] == 2:
        continue
    for j in range(i+1, N*M):
        if arr[j//M][j%M] == 1 or arr[j//M][j%M] == 2:
            continue
        for k in range(j+1, N*M):
            if arr[k//M][k%M] == 1 or  arr[k//M][k%M] == 2:
                continue
            for q in range(N):
                mat[q] = arr[q][:]

            mat[i//M][i%M] = 1
            mat[j//M][j%M] = 1
            mat[k//M][k%M] = 1
            logic = 1
            temp = 0 
            #print(i,j,k)
            while(logic):
                logic = 0
                for n in range(N):
                    for m in range(M):
                        if mat[n][m] == 2:
                            if n - 1 >= 0 and mat[n-1][m] == 0:
                                mat[n-1][m] = 2
                                logic = 1
                            if n + 1 < N and mat[n+1][m] == 0:
                                mat[n+1][m] = 2
                                logic = 1
                            if m - 1 >= 0 and mat[n][m-1] == 0:
                                mat[n][m-1] = 2
                                logic = 1
                            if m + 1 < M and mat[n][m+1] == 0:
                                mat[n][m+1] = 2
                                logic = 1
                            #print(temp)
                            #temp += 1

            result =0
            for n in range(N):
                for m in range(M):
                    if mat[n][m] == 0:
                        result += 1
            if result > result_max:
                result_max = result
                #print(result_max)
                #print(mat)
            mat[i//M][i%M] = 0
            mat[j//M][j%M] = 0
            mat[k//M][k%M] = 0

print(result_max)
