bit = [0, 0, 0, 0, 0]
max_num = 2
N = int(input())
mat = [list(map(int, input().split())) for _ in range(N)]
arr = [[] for _ in range(N)]
while bit[4] < 4:
    for i in range(N):
        arr[i] = mat[i][:]
    for i in range(4):
        if bit[i] == 4:
            bit[i] -= 4
            bit[i + 1] += 1
    for move in range(5):
        if bit[move] == 0:
            for i in range(N):
                for j in range(N):
                    if arr[i][j] == 0:
                        arr[i].pop(j)
                        arr[i].insert(0, 0)
            for i in range(N):
                for j in range(N-1, 0, -1):
                    if arr[i][j] == arr[i][j - 1] and arr[i][j] != 0:
                        arr[i][j] = arr[i][j] * 2
                        arr[i].pop(j-1)
                        arr[i].insert(0, 0)
            #print('')

        if bit[move] == 1:
            for i in range(N):
                for j in range(N-1, -1, -1):
                    if arr[i][j]== 0:
                        arr[i].pop(j)
                        arr[i].insert(N, 0)
            #print("")
            for i in range(N):
                for j in range(N-1):
                    if arr[i][j] == arr[i][j + 1] and arr[i][j] != 0:
                        arr[i][j] = arr[i][j] * 2
                        arr[i].pop(j+1)
                        arr[i].insert(N, 0)
            #print('')

        if bit[move] == 2:
            for i in range(N):
                last = -1
                pos = -1
                for j in range(N):
                    if arr[j][i] != 0:
                        if arr[j][i] != last:
                            last = arr[j][i]
                            pos = j
                        elif arr[j][i] != 0:
                            arr[pos][i] = arr[pos][i] * 2
                            arr[j][i] = 0
                            last = -1
                            pos = -1

            for i in range(N):
                zeros = 0
                for j in range(N):
                    if arr[j][i] == 0:
                        zeros += 1
                    else:
                        arr[j][i], arr[j - zeros][i] = arr[j - zeros][i], arr[j][i]
            #print("")

        if bit[move] == 3:
            for i in range(N):
                last = -1
                pos = -1
                for j in range(N-1, -1, -1):
                    if arr[j][i] != 0:
                        if arr[j][i] != last:
                            last = arr[j][i]
                            pos = j
                        elif arr[j][i] != 0:
                            arr[pos][i] = arr[pos][i] * 2
                            arr[j][i] = 0
                            last = -1
                            pos = -1

            for i in range(N):
                zeros = 0
                for j in range(N-1, -1, -1):
                    if arr[j][i] == 0:
                        zeros += 1
                    else:
                        arr[j + zeros][i], arr[j][i] = arr[j][i], arr[j + zeros][i]



    for i in range(N):
        if max(arr[i]) > max_num:
            max_num = max(arr[i])
    bit[0] += 1

print(max_num)