
dice = [0, 1,2,3,4,5,6]
x, y, d = 0, 0, 0
ans = 0


def go():
    global x, y, d, ans
    #change pos
    if d == 0:
        if y == m - 1:
            d = 2
            y -= 1
        else:
            y += 1

    elif d == 1:
        if x == n - 1:
            d = 3
            x -= 1
        else:
            x += 1

    elif d == 2:
        if y == 0:
            d = 0
            y += 1
        else:
            y -= 1

    elif d == 3:
        if x == 0:
            d = 1
            x += 1
        else:
            x -= 1    


    #change angle
    if d == 0:
        right()
    elif d == 1:
        down()
    elif d == 2:
        left()
    else:
        up()

    ans += get_point()

    d = change(d) 
    #print(ans,x, y, arr[x][y], '|', dice[6], dice[3], dice[1], dice[4], '|' ,dice[6], dice[2], dice[1], dice[5])

def right():
    temp = dice[1]
    dice[1] = dice[4]
    dice[4] = dice[6]
    dice[6] = dice[3]
    dice[3] = temp

def left():
    temp = dice[1]
    dice[1] = dice[3]
    dice[3] = dice[6]
    dice[6] = dice[4]
    dice[4] = temp

def up():
    temp = dice[2]
    dice[2] = dice[1]
    dice[1] = dice[5]
    dice[5] = dice[6]
    dice[6] = temp

def down():
    temp = dice[2]
    dice[2] = dice[6]
    dice[6] = dice[5]
    dice[5] = dice[1]
    dice[1] = temp

def change(d):
    if dice[6] > arr[x][y]:
        d = (d + 1) % 4
    elif dice[6] < arr[x][y]:
        d = (d + 3) % 4
    return d


def get_point():
    visit = [[0] * m for _ in range(n)]
    stack = [(x, y)]
    target = arr[x][y]
    visit[x][y] = 1
    res = 0
    while stack:
        a, b = stack.pop()
        if arr[a][b] == target:
            res += 1
            if a > 0 and visit[a -1][b] == 0:
                visit[a - 1][b] = 1
                stack.append((a - 1, b))
            if a < n - 1 and visit[a + 1][b] == 0:
                stack.append((a + 1, b))
                visit[a + 1][b] = 1
            if b > 0 and visit[a][b - 1] == 0:
                stack.append((a, b - 1))
                visit[a][b - 1] = 1
            if b < m - 1 and visit[a][b + 1] == 0:
                stack.append((a , b + 1))
                visit[a][b + 1] = 1
    return res * target


n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
#print(x, y, dice[6], arr[x][y], d, dice)  
while(k > 0):
    go()
    k -= 1
print(ans)

