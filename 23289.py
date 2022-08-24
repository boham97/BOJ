from pprint import pprint


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
while choco <100:
    for heat in heater_pos:
        if heat[2] == 1 and heat[1] + 1 < C:
            arr[heat[0]][heat[1]+1] += 5
            k = 5
            q = [[heat[0], heat[1]+1]]
            visit = [[heat[0], heat[1]+1]]
            while q and k > 0:
                v = q.pop(0)
                x, y = v[0],v[1]
                if y+1 <C:
                    k = 4 - y+1 + heat[1]
                if x-1 >= 0 and y+1 < C and [x, y, 1] not in wall_pos and [x-1,y+1,0] not in wall_pos and [x-1,y+1] not in visit:
                    arr[x-1][y+1] += k
                    q.append([x-1,y+1])
                    visit.append([x-1,y+1])
                if y+1 < C and [x,y+1,0] not in wall_pos and [x, y+1] not in visit:
                    arr[x][y+1] += k
                    q.append([x,y+1])
                    visit.append([x,y+1])
                if x+1 < R and y+1 < C and [x+1, y, 1] not in wall_pos and [x+1,y+1,0] not in wall_pos and [x+1,y+1] not in visit:
                    arr[x+1][y+1] += k
                    q.append([x+1,y+1])
                    visit.append([x+1,y+1])
        if heat[2] == 2:
            arr[heat[0]][heat[1]-1] += 5
            k = 5
            q = [[heat[0], heat[1]-1]]
            visit = [[heat[0], heat[1]-1]]
            while q and k > 0:
                v = q.pop(0)
                x, y = v[0],v[1]
                if y+1 <C:
                    k = 4 + y+1 - heat[1]
                if x-1 >= 0 and y-1 >= 0 and [x, y, 1] not in wall_pos and [x-1,y,0] not in wall_pos and [x-1,y-1] not in visit:
                    arr[x-1][y-1] += k
                    q.append([x-1,y-1])
                    visit.append([x-1,y-1])
                if y-1 >=0 and [x,y,0] not in wall_pos and [x, y-1] not in visit:
                    arr[x][y-1] += k
                    q.append([x,y-1])
                    visit.append([x,y-1])
                if x+1 < R and y-1 >= 0 and [x+1, y, 1] not in wall_pos and [x+1,y,0] not in wall_pos and [x+1,y-1] not in visit:
                    arr[x+1][y-1] += k
                    q.append([x+1,y-1])
                    visit.append([x+1,y-1])
        if heat[2] == 3:
            arr[heat[0]-1][heat[1]] += 5
            k = 5
            q = [[heat[0]-1, heat[1]]]
            visit = [[heat[0]-1, heat[1]]]
            while q and k > 0:
                v = q.pop(0)
                x, y = v[0],v[1]
                if x-1 <= 0:
                    k = 5 + x - heat[0]
                if x-1 >= 0 and y-1 >= 0 and [x, y-1, 1] not in wall_pos and [x,y,0] not in wall_pos and [x-1,y-1] not in visit:
                    arr[x-1][y-1] += k
                    q.append([x-1,y-1])
                    visit.append([x-1,y-1])
                if x-1 >=0 and [x,y,1] not in wall_pos and [x-1, y] not in visit:
                    arr[x-1][y] += k
                    q.append([x-1,y])
                    visit.append([x-1,y])
                if x-1 >=0 and y+1 < C and [x, y+1, 1] not in wall_pos and [x,y+1,0] not in wall_pos and [x-1,y+1] not in visit:
                    arr[x-1][y+1] += k
                    q.append([x-1,y+1])
                    visit.append([x-1,y+1])
        if heat[2] == 4:
            arr[heat[0]+1][heat[1]] += 5
            k = 5
            q = [[heat[0]+1, heat[1]]]
            visit = [[heat[0]+1, heat[1]]]
            while q and k > 0:
                v = q.pop(0)
                x, y = v[0],v[1]
                if x+1 <R:
                    k = 5 - x + heat[0]
                if x+1 < R and y-1 >= 0 and [x+1, y-1, 1] not in wall_pos and [x,y,0] not in wall_pos and [x+1,y-1] not in visit:
                    arr[x+1][y-1] += k
                    q.append([x+1,y-1])
                    visit.append([x+1,y-1])
                if x+1 <R and [x+1,y,1] not in wall_pos and [x+1, y] not in visit:
                    arr[x+1][y] += k
                    q.append([x+1,y])
                    visit.append([x+1,y])
                if x+1 <R and y+1 < C and [x+1, y+1, 1] not in wall_pos and [x,y+1,0] not in wall_pos and [x+1,y+1] not in visit:
                    arr[x+1][y+1] += k
                    q.append([x+1,y+1])
                    visit.append([x+1,y+1])
    for i in range(R):
        for j in range(C):
            cnt = 0
            temp = 0 
            if j-1 >= 0 and [i,j,0] not in wall_pos and :
                arr[i][j-1] 

    pprint(arr)