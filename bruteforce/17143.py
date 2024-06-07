import copy
def catch(c):
    for r in range(1, R + 1):
        if arr[r][c]:
            size = sharkes[arr[r][c]][2]
            arr[r][c] = 0
            return size
    return 0

        
def moveAll(t):
    for r in range(1, R + 1):
        for c in range(1, C + 1):
            if arr[r][c]:
                shark = arr[r][c]
                move(r, c, shark)
                
def move(r, c, shark):
    s, d, z = sharkes[shark]
    dr, dc = r, c
    if d == 1:
        dr += 2 * (R - dr)
        d = 2
    if d == 2:
        dr += s
        while 1 > dr or dr > R:
            if dr < 1:
                dr = 2 -dr
                d = 2
            else:
                d = 1
                dr = 2 * R - dr
    if d == 4:
        dc += 2 * (C - dc)
        d = 3
    if d == 3:
        dc += s
        while 1 > dc or dc > C:
            if dc < 1:
                dc = 2 -dc
                d = 3
            else:
                d = 4
                dc = 2 * C - dc
    if temp[dr][dc]:
        temp[dr][dc] = temp[dr][dc] if sharkes[temp[dr][dc]][2] > z else shark
    else:
        temp[dr][dc] = shark
    sharkes[shark] = [s, d, z]


ans = 0
R, C, M = map(int, input().split())
arr = [[0] * (C + 1) for _ in range(R + 1)]
sharkes = []
sharkes.append((0,0,0,0))
for i in range(1, M + 1):
    r, c, s, d, z = map(int, input().split())
    sharkes.append([s, d, z])
    arr[r][c] = i


for i in range(1, C + 1):
    temp = [[0] * (C + 1) for _ in range(R + 1)]
    ans += catch(i)
    moveAll(i)
    arr = copy.copy(temp)

print(ans)
