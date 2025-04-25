from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


def bfs():
    global ans
    while que:
        Rx, Ry, Bx, By = que.popleft()
        turn = visit[Rx * 1000 + Ry * 100 + Bx * 10 + By]
        if turn > 10:
            continue
        arr[Rx][Ry] = 'R'
        arr[Bx][By] = 'B'
        for i in range(4):
            if (i == 0 and Rx < Bx) or (i == 1 and Rx > Bx) or (i == 2 and Ry > By) or (i == 3 and Ry < By):
                Rx_temp, Ry_temp = go(Rx, Ry, i, 'R')
                Bx_temp, By_temp = go(Bx, By, i, 'B')
            else:
                Bx_temp, By_temp = go(Bx, By, i, 'B')
                Rx_temp, Ry_temp = go(Rx, Ry, i, 'R')

            if Rx_temp != Ox or Ry_temp != Oy:
                arr[Rx_temp][Ry_temp] = '.'
            if Bx_temp != Ox or By_temp != Oy:
                arr[Bx_temp][By_temp] = '.'
            arr[Rx][Ry] = 'R'
            arr[Bx][By] = 'B'
            if Rx_temp == Ox and Ry_temp == Oy and (Bx_temp != Ox or By_temp != Oy):
                if ans > turn + 1:
                    ans = turn + 1
                    print(1)
                    exit()
            elif Bx == Ox and By == Oy:
                pass
            elif (
                    Bx_temp != Ox or By_temp != Oy) and Rx_temp * 1000 + Ry_temp * 100 + Bx_temp * 10 + By_temp not in visit:
                visit[Rx_temp * 1000 + Ry_temp * 100 + Bx_temp * 10 + By_temp] = turn + 1
                que.append([Rx_temp, Ry_temp, Bx_temp, By_temp])
        arr[Rx][Ry] = '.'
        arr[Bx][By] = '.'


def go(x, y, i, color):
    while arr[x + dx[i]][y + dy[i]] == '.' or arr[x + dx[i]][y + dy[i]] == 'O':
        arr[x][y] = '.'
        x, y = x + dx[i], y + dy[i]
        if arr[x][y] == 'O':
            return (x, y)
        else:
            arr[x][y] = color
    return (x, y)


N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'R':
            Rx, Ry = i, j
        if arr[i][j] == 'B':
            Bx, By = i, j
        if arr[i][j] == 'O':
            Ox, Oy = i, j

que = deque()
visit = {Rx * 1000 + Ry * 100 + Bx * 10 + By: 0}

ans = 11
que.append([Rx, Ry, Bx, By])
bfs()
if ans == 11:
    print(0)
else:
    print(1)