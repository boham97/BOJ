import sys
input = sys.stdin.readline
move = [[0,1,1,1,0,0,0,-1,-1,-1], [0,-1,0,1,-1,0,1,-1,0,1]]
n, m = map(int, input().split())

arr = list(list(input().rstrip()) for _ in range(n))
order = list(map(int, list(input().rstrip())))

x, y = 0, 0
robot  = set()
nxt, destroy = set(), set()

for i in range(n):
    for j in range(m):
        if arr[i][j] == 'I':
            x, y = i, j
        elif arr[i][j] == 'R':
            robot.add((i,j))

for i in range(len(order)):
    arr[x][y] = '.'
    x, y = x + move[0][order[i]], y+ move[1][order[i]]
    if arr[x][y] == 'R':
        print("kraj", i + 1)
        exit()
    arr[x][y] = 'I'

    nxt.clear()
    destroy.clear()
    for a,b in robot:
        cost = n*m
        direct = 0
        if arr[a][b] == '.':
            continue
        arr[a][b] = '.'
        for k in range(10):
            temp = abs(x - a - move[0][k] ) + abs(y - b - move[1][k])
            if temp < cost:
                cost = temp
                direct = k
        da = a + move[0][direct]
        db = b + move[1][direct]

        if arr[da][db] == 'I':
            print("kraj", i + 1)
            exit()
        
        if (da, db) in nxt:
            destroy.add((da,db))
        else:
            nxt.add((da,db))
        

        
    robot = nxt - destroy
    for da, db in robot:
        arr[da][db] = 'R'

for j in range(n):
    for k in range(m):
        print(arr[j][k], end= '')
    print()

