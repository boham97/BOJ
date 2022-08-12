N, M = list(map(int, input().split()))
input_arr = [[] for _ in range(N)]
for i in range(N):
    input_arr[i] = list(map(int, input().split()))
cctv = []
angle = []
for i in range(N):
    for j in range(M):
        if input_arr[i][j] == 1:
            cctv.append([i, j, input_arr[i][j], [0]])
            angle.append([0])
        elif input_arr[i][j] == 2:
            cctv.append([i, j, input_arr[i][j], [0, 2]])
            angle.append([0, 2])
        elif input_arr[i][j] == 3:
            cctv.append([i, j, input_arr[i][j], [0, 1]])
            angle.append([0, 1])
        elif input_arr[i][j] == 4:
            cctv.append([i, j, input_arr[i][j], [0, 1, 2]])
            angle.append([0, 1, 2])
        elif input_arr[i][j] == 5:
            cctv.append([i, j, input_arr[i][j], [0, 1, 2, 3]])
            angle.append([0, 1, 2, 3])

bit_arr = []
max_iter = 1
for i in range(len(cctv)):
    if cctv[i][2] == 1:
        bit_arr.append(4)
        max_iter = max_iter * 4
    elif cctv[i][2] == 2:
        bit_arr.append(2)
        max_iter = max_iter * 2
    elif cctv[i][2] == 3:
        bit_arr.append(4)
        max_iter = max_iter * 4
    elif cctv[i][2] == 4:
        bit_arr.append(4)
        max_iter = max_iter * 4
    elif cctv[i][2] == 5:
        bit_arr.append(1)
logic = 0
bit = [0] * len(bit_arr)
mat = [[] for _ in range(N)]
min_area = N * M
for iteration in range(max_iter):
    for i in range(N):
        mat[i] = input_arr[i][:]

    for i in range(len(bit_arr)):
        if bit[i] == bit_arr[i]:
            bit[i] = 0
            bit[i+1] += 1

    for i in range(len(angle)):
        for j in range(len(angle[i])):
            angle[i][j] = (cctv[i][3][j] +bit[i]) % 4
    #print(angle)
    # angle OK!
    for i in range(len(angle)):
        for j in range(len(angle[i])):
            if angle[i][j] == 0:
                k = cctv[i][1]
                while k < M and mat[cctv[i][0]][k] != 6:
                    if mat[cctv[i][0]][k] == 0:
                        mat[cctv[i][0]][k] = '#'
                    k += 1
            if angle[i][j] == 1:
                k = cctv[i][0]
                while k >= 0 and mat[k][cctv[i][1]] != 6:
                    if mat[k][cctv[i][1]] == 0:
                        mat[k][cctv[i][1]] = '#'
                    k -= 1
            if angle[i][j] == 2:
                k = cctv[i][1]
                while k >= 0 and mat[cctv[i][0]][k] != 6:
                    if mat[cctv[i][0]][k] == 0:
                        mat[cctv[i][0]][k] = '#'
                    k -= 1
            if angle[i][j] == 3:
                k = cctv[i][0]
                while k < N and mat[k][cctv[i][1]] != 6:
                    if mat[k][cctv[i][1]] == 0:
                        mat[k][cctv[i][1]] = '#'
                    k += 1
    cnt = 0
    for i in range(N):
        for j in range(M):
            if mat[i][j] == 0:
                cnt += 1
    if cnt < min_area:
        min_area = cnt
    if len(bit) == 0:
        break
    bit[0] += 1

    # ok!
print(min_area)