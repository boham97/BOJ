# 다시 풀기 :(

N, M, R = list(map(int,input().split()))

mat = [list(map(int,input().split())) for _ in range(N)]

orders = list(map(int,input().split()))
turn = 0
mirror = 0
arr = [0, 1, 2, 3]
for order in orders:
    if order == 1:
        arr[0], arr[1], arr[2], arr[3] = arr[3], arr[2], arr[1], arr[0]
        mirror += 1
    elif order == 2:
        arr[0], arr[1], arr[2], arr[3] = arr[1], arr[0], arr[3], arr[2]
        mirror += 1
        turn +=2
    elif order == 3:
        arr[0], arr[1], arr[2], arr[3] = arr[3], arr[0], arr[1], arr[2]
        turn += 1
    elif order == 4:
        arr[0], arr[1], arr[2], arr[3] = arr[1], arr[2], arr[3], arr[0]
        turn += 3
    elif order == 5:
        arr[0], arr[1], arr[2], arr[3] = arr[3], arr[0], arr[1], arr[2]
    elif order == 6:
        arr[0], arr[1], arr[2], arr[3] = arr[1], arr[2], arr[3], arr[0]

mat1 =[[0 for j in range(M//2)] for _ in range(N//2)]
for i in range(N//2):
    for j in range(M//2):
        mat1[i][j] = mat[i][j]
mat2 =[[0 for j in range(M//2)] for _ in range(N//2)]
for i in range(N//2):
    for j in range(M//2):
        mat2[i][j] = mat[i][j+ M//2]
mat3 =[[0 for j in range(M//2)] for _ in range(N//2)]
for i in range(N//2):
    for j in range(M//2):
        mat3[i][j] = mat[i + N//2][j + M//2]
mat4 =[[0 for j in range(M//2)] for _ in range(N//2)]
for i in range(N//2):
    for j in range(M//2):
        mat4[i][j] = mat[i + N//2][j]
big_mat= [mat1, mat2, mat3, mat4]
#print(big_mat)

for i in range(mirror%2):
    for j in range(4):
        for x in range(len(big_mat[j])//2):
            for y in range(len(big_mat[j][0])):
                big_mat[j][x][y], big_mat[j][len(big_mat[j])-x-1][y] = big_mat[j][len(big_mat[j])-x-1][y], big_mat[j][x][y]
#print(big_mat)


for i in range(turn%4):
    for j in range(4):
        temp = [[0 for k in range(len(big_mat[j]))] for m in range(len(big_mat[j][0]))]
        for x in range(len(big_mat[j])):
            for y in range(len(big_mat[j][0])):
                temp[y][len(big_mat[j])-x-1] = big_mat[j][x][y]
        n =len(big_mat[j][0])
        big_mat[j]=[]
        for k in range(n):
            big_mat[j].append(temp[k][:])
    #print(big_mat)
    #print()



result = [[0 for i in range(len(big_mat[0][0])*2)] for j in range(len(big_mat[0])*2)]

for i in range(len(big_mat[0])):
    for j in range(len(big_mat[0][0])):
        #print(big_mat[arr[0]][i][j])
        result[i][j] = big_mat[arr[0]][i][j]

for i in range(len(big_mat[0])):
    for j in range(len(big_mat[0][0])):
        result[i][j + len(big_mat[0][0])] = big_mat[arr[1]][i][j]

for i in range(len(big_mat[0])):
    for j in range(len(big_mat[0][0])):
        result[i + len(big_mat[0])][j + len(big_mat[0][0])] = big_mat[arr[2]][i][j]

for i in range(len(big_mat[0])):
    for j in range(len(big_mat[0][0])):
        result[i + len(big_mat[0])][j] = big_mat[arr[3]][i][j]

for i in range(len(result)):
    print(*result[i])