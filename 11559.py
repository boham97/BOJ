from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

arr = list(list(input()) for _ in range(12))

change = 1
ans = 0

while change:
    visit = [[1] * 6 for _ in range(12)]
    change = 0
    for i in range(12):
        for j in range(6):
            que = deque()
            poplist = []
            if arr[i][j] != "." and visit[i][j]:
                visit[i][j] = 0
                poplist.append((i,j))
                que.append((i,j))
                while que:
                    x, y = que.popleft()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0<= nx < 12 and  0<=ny <6 and arr[i][j] == arr[nx][ny] and visit[nx][ny]:
                            que.append((nx,ny))
                            poplist.append((nx,ny))
                            visit[nx][ny] = 0
                if len(poplist) > 3:
                    for targetx, targety in poplist:
                        arr[targetx][targety] = "."
                    change = 1

    for j in range(6):
        temp = []
        for i in range(12):
            if arr[i][j] != ".":
                temp.append(arr[i][j])
                arr[i][j] = "."
        for i in range(len(temp)):
            arr[11-i][j] = temp.pop()
    if change:
        ans += 1


print(ans)
                    
