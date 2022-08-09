R, C, K = list(map(int,input().split()))

arr = [[] for _ in range(R)]

for r in range(R):
    arr[r] = list(map(int,input().split()))
walls = int(input())
wall_pos = []
for i in range(walls):
    wall_pos.append(list(map(int,input().split())))
    wall_pos[len(wall_pos)-1][0] -= 1
    wall_pos[len(wall_pos)-1][1] -= 1
test_pos = []
heater_pos = []
for r in range(R):
    for c in range(C):
        if arr[r][c] == 5:
            test_pos.append([r,c])
            arr[r][c] = 0
        elif arr[r][c] > 0:
            heater_pos.append([r, c, arr[r][c]])
            arr[r][c] = 0
#print(wall_pos, '\n', test_pos, '\n', heater_pos)  #OK!

for heat in heater_pos:
    if heat[2] == 1:
        arr[heat[0]][heat[1]] += 1
        for i in range(1,6):
            for j in range(i):
                if heat[1]+i < C and heat[0] - j >= 0:
                    if arr[heat[0] - j][heat[1] + i - 1] > 0 and [heat[0] - j, heat[1] + i - 1, 1] not in wall_pos:
                        arr[heat[0] - j][heat[1] + i] += 6 -i
                    elif heat[0] - j - 1 >= 0 and arr[heat[0] - j - 1][heat[1] + i - 1] > 0 and [heat[0] - j, heat[1] + i - 1, 0] not in wall_pos and [heat[0] - j, heat[1] + i - 1, 1] not in wall_pos:
                        arr[heat[0] - j][heat[1] + i] += 6 -i
                    elif arr[heat[0] - j + 1][heat[1] + i - 1] > 0 and [heat[0] - j + 1, heat[1] + i - 1, 0] not in wall_pos and [heat[0] - j, heat[1] + i - 1, 1] not in wall_pos:
                        arr[heat[0] - j][heat[1] + i] += 6 -i
                if heat[1] + i < C and heat[0] + j < R and j > 0:
                    if arr[heat[0] + j][heat[1] + i - 1] > 0 and [heat[0] + j, heat[1] + i - 1, 1] not in wall_pos:
                        arr[heat[0] + j][heat[1] + i] += 6 -i
                    elif heat[0] + j - 1 >= 0 and arr[heat[0] + j - 1][heat[1] + i - 1] > 0 and [heat[0] + j, heat[1] + i - 1, 0] not in wall_pos and [heat[0] + j, heat[1] + i - 1, 1] not in wall_pos:
                        arr[heat[0] + j][heat[1] + i] += 6 -i
                    elif heat[0] + j + 1<R and arr[heat[0] + j + 1][heat[1] + i - 1] > 0 and [heat[0] + j + 1, heat[1] + i - 1, 0] not in wall_pos and [heat[0] + j, heat[1] + i - 1, 1] not in wall_pos:
                        arr[heat[0] + j][heat[1] + i] += 6 -i
        arr[heat[0]][heat[1]] -= 1

    if heat[2] == 2:
        arr[heat[0]][heat[1]] += 1
        for i in range(1,6):
            for j in range(i):
                if heat[1] - i >= 0 and heat[0] - j >= 0:
                    if arr[heat[0] - j][heat[1] - i + 1] > 0 and [heat[0] - j, heat[1] - i, 1] not in wall_pos:
                        arr[heat[0] - j][heat[1] - i] += 6 -i
                    elif heat[0] - j - 1 >= 0 and arr[heat[0] - j - 1][heat[1] - i + 1] > 0 and [heat[0] - j, heat[1] - i + 1, 0] not in wall_pos and [heat[0] - j, heat[1] - i, 1] not in wall_pos:
                        arr[heat[0] - j][heat[1] - i] += 6 -i
                    elif arr[heat[0] - j + 1][heat[1] - i + 1] > 0 and [heat[0] - j + 1, heat[1] - i + 1, 0] not in wall_pos and [heat[0] - j, heat[1] - i, 1] not in wall_pos:
                        arr[heat[0] - j][heat[1] - i] += 6 -i
                if heat[1] - i >= 0 and heat[0] + j < R and j > 0:
                    if arr[heat[0] + j][heat[1] - i + 1] > 0 and [heat[0] + j, heat[1] - i, 1] not in wall_pos:
                        arr[heat[0] + j][heat[1] - i] += 6 -i
                    elif heat[0] + j - 1 >= 0 and arr[heat[0] + j - 1][heat[1] - i + 1] > 0 and [heat[0] + j, heat[1] - i + 1, 0] not in wall_pos and [heat[0] + j, heat[1] - i, 1] not in wall_pos:
                        arr[heat[0] + j][heat[1] - i] += 6 -i
                    elif heat[0] + j + 1 < R and arr[heat[0] + j + 1][heat[1] - i + 1] > 0 and [heat[0] + j + 1, heat[1] - i + 1, 0] not in wall_pos and [heat[0] + j, heat[1] - i, 1] not in wall_pos:
                        arr[heat[0] + j][heat[1] - i] += 6 -i
        arr[heat[0]][heat[1]] -= 1

    if heat[2] == 3:
        arr[heat[0]][heat[1]] += 1
        for i in range(1,6):
            for j in range(i):
                if heat[0] - i >= 0 and heat[1] - j >= 0:
                    if arr[heat[0] - i + 1][heat[1] - j] > 0 and [heat[0] - i + 1, heat[1] - j, 0] not in wall_pos:
                        arr[heat[0] - i][heat[1] - j] += 6 -i
                    elif heat[1] - j - 1 >= 0 and arr[heat[0] - i + 1][heat[1] - j - 1] > 0 and [heat[0] - i + 1, heat[1] - j, 0] not in wall_pos and [heat[0] - i + 1, heat[1] - j - 1, 1] not in wall_pos:
                        arr[heat[0] - i][heat[1] - j] += 6 -i
                    elif arr[heat[0] - i + 1][heat[1] - j + 1] > 0 and [heat[0] - i + 1, heat[1] - j, 0] not in wall_pos and [heat[0] - i + 1, heat[1] - j, 1] not in wall_pos:
                        arr[heat[0] - i][heat[1] - j] += 6 -i
                if heat[0] - i >= 0 and heat[1] + j < C and j > 0:
                    if arr[heat[0] - i + 1][heat[1] + j] > 0 and [heat[0] - i + 1, heat[1] - j, 0] not in wall_pos:
                        arr[heat[0] - i][heat[1] + j] += 6 -i
                    elif heat[1] + j - 1 >= 0 and arr[heat[0] - i + 1][heat[1] - j + 1] > 0 and [heat[0] + j, heat[1] - i + 1, 0] not in wall_pos and [heat[0] + j, heat[1] - i, 1] not in wall_pos:
                        arr[heat[0] + j][heat[1] - i] += 6 -i
                    elif heat[0] + j + 1 < R and arr[heat[0] + j + 1][heat[1] - i + 1] > 0 and [heat[0] + j + 1, heat[1] - i + 1, 0] not in wall_pos and [heat[0] + j, heat[1] - i, 1] not in wall_pos:
                        arr[heat[0] + j][heat[1] - i] += 6 -i
        arr[heat[0]][heat[1]] -= 1



print()
for i in range(R):
    for j in range(C):
        print(arr[i][j], end=' ')
    print()