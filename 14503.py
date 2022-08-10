N, M = map(int,input().split())
X, Y, direction = map(int,input().split())

arr = [[] for _ in range(N)]
for i in range(N):
    arr[i] = list(map(int,input().split()))
drc = [[-1, 0], [0, 1], [1, 0], [0, -1] ]
cnt = 0

while(1):
    if arr[X][Y] == 0:
        arr[X][Y] = 2
        cnt += 1

    if arr[X + drc[(direction + 4 - 1) % 4][0]][Y + drc[(direction + 4 - 1) % 4][1]] == 0:
        X = X + drc[(direction + 4 - 1) % 4][0]
        Y = Y + drc[(direction + 4 - 1) % 4][1]
        direction = (direction + 4 - 1) % 4
    elif arr[X-1][Y] != 0 and arr[X][Y - 1] != 0 and arr[X][Y + 1] != 0 and arr[X + 1][Y] != 0:
        if arr[X + drc[(direction + 4 - 2) % 4][0]][Y + drc[(direction + 4 - 2) % 4][1]] == 1:
            break
        else:
            X = X + drc[(direction + 4 - 2) % 4][0]
            Y = Y + drc[(direction + 4 - 2) % 4][1]
    elif arr[X + drc[(direction + 4 - 1) % 4][0]][Y + drc[(direction + 4 - 1) % 4][1]] != 0:
        direction = (direction + 4 - 1) % 4

print(cnt)
