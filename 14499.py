q1 = [0,0,0,0] #가로
q2 = [0,0,0,0] #세로
N, M, x, y,temp = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
dy = [0, 1, -1, 0, 0]
dx = [0, 0, 0, -1, 1]
orders = list(map(int,input().split()))

for order in orders:
    if 0 <= x+dx[order] < N and 0 <= y+dy[order] < M:
        x, y = x+dx[order], y+ dy[order]
        if order == 4:
            q1.insert(0,q1.pop())
            q2[3] = q1[3]
            q2[1] = q1[1]
        elif order == 3:
            q1.append(q1.pop(0))
            q2[3] = q1[3]
            q2[1] = q1[1]
        elif order == 2:
            q2.append(q2.pop(0))
            q1[3] = q2[3]
            q1[1] = q2[1]
        elif order == 1:
            q2.insert(0,q2.pop())
            q1[3] = q2[3]
            q1[1] = q2[1]
        if arr[x][y] == 0:
            arr[x][y] = q1[3]
            q2[3] = q1[3]
        else:
            q1[3] = arr[x][y]
            q2[3] = q1[3]
            arr[x][y] = 0
        print(q1[1])