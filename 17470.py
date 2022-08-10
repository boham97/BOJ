# 다시 풀기 :(

N, M, R = list(map(int,input().split()))

mat = [[] for _ in range(N)]

for i in range(N):
    mat[i] = list(map(int,input().split()))

orders = list(map(int,input().split()))
turn = 0
mirror = 0
arr =[0, 1, 2, 3]
orderlist =[0, 0, 0, 0, 0, 0, 0,]
for order in orders:
    orderlist[order] += 1

order1 = orderlist[1] % 2
order2 = orderlist[2] % 2
order3 = (orderlist[3] + orderlist[5] + orderlist[4] * 3 + orderlist[6] * 3) % 4
mirror = (orderlist[1] + orderlist[2]) % 2
turn = (orderlist[2] * 2 + orderlist[3] + orderlist[4] * 3) % 4

if order1 == 1:
    arr[0], arr[1], arr[2], arr[3] = arr[3], arr[2], arr[1], arr[0]
if order2 == 1:
    arr[0], arr[1], arr[2], arr[3] = arr[1], arr[0], arr[3], arr[2]
for i in range(order3):
    arr[0], arr[1], arr[2], arr[3] = arr[3], arr[0], arr[1], arr[2]

""" if order == 3:
    arr[0], arr[1], arr[2], arr[3] = arr[3], arr[0], arr[1], arr[2]
    turn += 1
if order == 4:
    arr[0], arr[1], arr[2], arr[3] = arr[1], arr[2], arr[3], arr[0]
    turn += 3
if order == 5:
    arr[0], arr[1], arr[2], arr[3] = arr[3], arr[0], arr[1], arr[2]
if order == 6:
    arr[0], arr[1], arr[2], arr[3] = arr[1], arr[2], arr[3], arr[0] """

#print(arr, mirror, turn)

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

for i in range(mirror):
    for j in range(4):
        for x in range(len(big_mat[j])//2):
            for y in range(len(big_mat[j][0])):
                big_mat[j][x][y], big_mat[j][len(big_mat[j])-x-1][y] = big_mat[j][len(big_mat[j])-x-1][y], big_mat[j][x][y]
#print(big_mat)


for i in range(turn):
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


for i in range(len(big_mat[0])*2):
    for j in range(len(big_mat[0][0])*2):
        print(result[i][j], end='')
        if j < len(big_mat[0][0])*2 - 1:
            print(end= ' ')
    if i < len(big_mat[0])*2 - 1:
        print()