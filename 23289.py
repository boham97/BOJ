#from pprint import pprint
R, C, K = list(map(int, input().split()))
arr = [[] for _ in range(R)]
for r in range(R):
    arr[r] = list(map(int, input().split()))
walls = int(input())
wall_pos = []
for i in range(walls):
    wall_pos.append(list(map(int, input().split())))
    wall_pos[len(wall_pos)-1][0] -= 1
    wall_pos[len(wall_pos)-1][1] -= 1
test_pos = []
heater_pos = []
for r in range(R):
    for c in range(C):
        if arr[r][c] == 5:
            test_pos.append([r, c])
            arr[r][c] = 0
        elif arr[r][c] > 0:
            heater_pos.append([r, c, arr[r][c]])
            arr[r][c] = 0
    '''print(wall_pos, '\n', test_pos, '\n', heater_pos)  #OK!'''
choco = 0
while choco <=100:
    for heat in heater_pos:
        if heat[2] == 1 and heat[1] + 1 < C:
            arr[heat[0]][heat[1]+1] += 5
            k = 5
            q = [[heat[0], heat[1]+1]]
            visit = [[0]* C for _ in range(R)]
            visit[heat[0]][heat[1]+1] = 1
            while q and k > 0:
                v = q.pop(0)
                x, y = v[0],v[1]
                if y+1 <C:
                    k = 4 - y+1 + heat[1]
                if x-1 >= 0 and y+1 < C and [x, y, 0] not in wall_pos and [x-1,y,1] not in wall_pos and visit[x-1][y+1] == 0:
                    arr[x-1][y+1] += k
                    q.append([x-1,y+1])
                    visit[x-1][y+1] = 1
                if y+1 < C and [x,y,1] not in wall_pos and visit[x][y+1] == 0:
                    arr[x][y+1] += k
                    q.append([x,y+1])
                    visit[x][y+1] = 1
                if x+1 < R and y+1 < C and [x+1, y, 0] not in wall_pos and [x+1,y,1] not in wall_pos and visit[x+1][y+1] == 0:
                    arr[x+1][y+1] += k
                    q.append([x+1,y+1])
                    visit[x+1][y+1] = 1
        if heat[2] == 2:
            arr[heat[0]][heat[1]-1] += 5
            k = 5
            q = [[heat[0], heat[1]-1]]
            visit = [[0]*C for _ in range(R)]
            visit[heat[0]][heat[1]-1] = 1
            while q and k > 0:
                v = q.pop(0)
                x, y = v[0],v[1]
                if y+1 <C:
                    k = 4 + y+1 - heat[1]
                if x-1 >= 0 and y-1 >= 0 and [x, y, 0] not in wall_pos and [x-1,y-1,1] not in wall_pos and visit[x-1][y-1] == 0:
                    arr[x-1][y-1] += k
                    q.append([x-1,y-1])
                    visit[x-1][y-1] = 1
                if y-1 >=0 and [x,y-1,1] not in wall_pos and visit[x][y-1] == 0:
                    arr[x][y-1] += k
                    q.append([x,y-1])
                    visit[x][y-1] = 1
                if x+1 < R and y-1 >= 0 and [x+1, y, 0] not in wall_pos and [x+1,y-1,1] not in wall_pos and visit[x+1][y-1] == 0:
                    arr[x+1][y-1] += k
                    q.append([x+1,y-1])
                    visit[x+1][y-1] = 1
        if heat[2] == 3:
            arr[heat[0]-1][heat[1]] += 5
            k = 5
            q = [[heat[0]-1, heat[1]]]
            visit = [[0]*C for _ in range(R)]
            visit[heat[0]-1][heat[1]] = 1
            while q and k > 0:
                v = q.pop(0)
                x, y = v[0], v[1]
                if x-1 >= 0:
                    k = 5 + x - heat[0]
                if x-1 >= 0 and y-1 >= 0 and [x, y-1, 0] not in wall_pos and [x,y-1,1] not in wall_pos and visit[x-1][y-1] == 0:
                    arr[x-1][y-1] += k
                    q.append([x-1,y-1])
                    visit[x-1][y-1] = 1
                if x-1 >=0 and [x,y,0] not in wall_pos and visit[x-1][ y] == 0:
                    arr[x-1][y] += k
                    q.append([x-1,y])
                    visit[x-1][y] = 1
                if x-1 >=0 and y+1 < C and [x, y+1, 0] not in wall_pos and [x,y,1] not in wall_pos and visit[x-1][y+1] == 0:
                    arr[x-1][y+1] += k
                    q.append([x-1,y+1])
                    visit[x-1][y+1] = 1
        if heat[2] == 4:
            arr[heat[0]+1][heat[1]] += 5
            k = 5
            q = [[heat[0]+1, heat[1]]]
            visit = [[0] *C for _ in range(R)]
            visit[heat[0]+1][heat[1]] = 1
            while q and k > 0:
                v = q.pop(0)
                x, y = v[0],v[1]
                if x+1 <R:
                    k = 5 - x + heat[0]
                if x+1 < R and y-1 >= 0 and [x, y-1, 1] not in wall_pos and [x+1,y-1,0] not in wall_pos and visit[x+1][y-1] == 0:
                    arr[x+1][y-1] += k
                    q.append([x+1,y-1])
                    visit[x+1][y-1] =1
                if x+1 <R and [x+1,y,0] not in wall_pos and visit[x+1][y] == 0:
                    arr[x+1][y] += k
                    q.append([x+1,y])
                    visit[x+1][y] = 1
                if x+1 <R and y+1 < C and [x+1, y+1, 0] not in wall_pos and [x,y,1] not in wall_pos and visit[x+1][y+1] == 0:
                    arr[x+1][y+1] += k
                    q.append([x+1,y+1])
                    visit[x+1][y+1] = 1
    temp = [[0] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if j-1 >= 0 and [i,j-1,1] not in wall_pos and arr[i][j]> arr[i][j-1]:
                temp[i][j-1] += (arr[i][j] - arr[i][j-1])//4
                temp[i][j] -= (arr[i][j] - arr[i][j-1])//4
            if i-1 >= 0 and [i,j,0] not in wall_pos and arr[i][j]> arr[i-1][j]:
                temp[i-1][j] += (arr[i][j] - arr[i-1][j])//4
                temp[i][j] -= (arr[i][j] - arr[i-1][j])//4
            if j+1 < C and [i,j,1] not in wall_pos and arr[i][j]> arr[i][j+1]:
                temp[i][j+1] += (arr[i][j] - arr[i][j+1])//4
                temp[i][j] -= (arr[i][j] - arr[i][j+1])//4
            if i+1 < R and [i+1,j,0] not in wall_pos and arr[i][j]> arr[i+1][j]:
                temp[i+1][j] += (arr[i][j] - arr[i+1][j])//4
                temp[i][j] -= (arr[i][j] - arr[i+1][j])//4
    for i in range(R):
        for j in range(C):
            arr[i][j] += temp[i][j]
    for i in range(R):
        if arr[i][0] != 0:
            arr[i][0] -= 1
        if arr[i][C-1] != 0:
            arr[i][C-1] -= 1
    for i in range(1,C-1):
        if arr[0][i] != 0:
            arr[0][i] -= 1
        if arr[R-1][i] != 0:
            arr[R-1][i] -= 1
    choco +=1
    cnt = 0
    for test in test_pos:
        x, y =test[0], test[1]
        if arr[x][y] >= K:
            cnt += 1
    if cnt == len(test_pos):
        break
print(choco)
#pprint(arr)