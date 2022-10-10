import sys

N, M, R = list(map(int,input().split()))

mat = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

orders = list(map(int,sys.stdin.readline().split()))
turn_list = [[0,1,2,3],[3,0,1,2],[2,3,0,1],[1,2,3,0]]
arr = [0,1,2,3]
turn = [0,1,2,3]
for order in orders:
    if order == 1:
        arr[0], arr[1], arr[2],arr[3] = arr[3],arr[2],arr[1],arr[0]
        turn[0], turn[1], turn[2], turn[3] = turn[3], turn[2], turn[1], turn[0]
    elif order == 2:
        arr[0], arr[1], arr[2],arr[3] = arr[1], arr[0], arr[3], arr[2]
        turn[0], turn[1], turn[2], turn[3] = turn[1], turn[0], turn[3], turn[2]
    elif order == 3:
        arr[0], arr[1], arr[2],arr[3] = arr[3], arr[0], arr[1], arr[2]
        turn[0], turn[1], turn[2], turn[3] = turn[3], turn[0], turn[1], turn[2]
    elif order == 4:
        arr[0], arr[1], arr[2],arr[3] = arr[1], arr[2], arr[3], arr[0]
        turn[0], turn[1], turn[2], turn[3] = turn[1], turn[2], turn[3], turn[0]
    elif order == 5:
        arr[0], arr[1], arr[2],arr[3] = arr[3], arr[0], arr[1], arr[2]
    elif order == 6:
        arr[0], arr[1], arr[2],arr[3] = arr[1], arr[2], arr[3], arr[0]
temp = [[[0] * (M//2) for _ in range(N//2)] for _ in range(4)]
for i in range(N//2):
    temp[0][i] = mat[i][:(M//2)]
    temp[1][i] = mat[i][(M//2):M]
    temp[2][i] = mat[i+N//2][(M//2):M]
    temp[3][i] = mat[i+N//2][:(M//2)]
flag = 0
if turn not in turn_list:
    flag = 1
    turn[0], turn[1], turn[2], turn[3] = turn[3], turn[2], turn[1], turn[0]
    for j in range(4):
        temp[j] = temp[j][::-1]

for l in range(4):
    iter = turn_list.index(turn)
    if flag:
        iter = 4 - iter
    for i in range(iter):
        x = len(temp[l])
        y = len(temp[l][0])
        temp2 = [[0]*x for _ in range(y)]
        for j in range(x):
            for k in range(y):
                temp2[k][x-j-1] = temp[l][j][k]
        temp[l] = [[0]*x for _ in range(y)]
        for j in range(y):
            temp[l][j] = temp2[j][:]

for i in range(len(temp[0])):
    print(*temp[arr[0]][i],*temp[arr[1]][i])
for i in range(len(temp[3])):
    print(*temp[arr[3]][i],*temp[arr[2]][i])