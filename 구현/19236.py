delta = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]

def move(arr, fish):
    for i in range(17):
        if i not in fish:
            continue
        x, y, d = fish[i]
        for _ in range(8):
            nx, ny = x + delta[d][0], y + delta[d][1]
            if 0 <= nx < 4 and 0 <= ny < 4 and arr[nx][ny] != -1:
                if arr[nx][ny] == 0:
                    arr[x][y], arr[nx][ny] = 0, i
                    fish[i] = (nx, ny, d)
                else:
                    j = arr[nx][ny] 
                    arr[x][y], arr[nx][ny] = j, i
                    fish[i] = (nx, ny, d)
                    fish[j] = (x, y, fish[j][2])
                break
            d = (d + 1) % 8



def dfs(arr, shark, fish, total, depth=0):
    global result
    result = max(result, total)
    arr = [row[:] for row in arr]
    fish = fish.copy()
    move(arr, fish)
    x, y, d = shark
    for step in range(1, 4):
        nx, ny = x + delta[d][0] * step, y + delta[d][1] * step
        if 0 <= nx < 4 and 0 <= ny < 4 and arr[nx][ny] != 0:
            temp = arr[nx][ny]

            arr[x][y], arr[nx][ny] = 0, -1
            shark_next = (nx, ny, fish[temp][2])
            fish.pop(temp)
            dfs(arr, shark_next, fish, total + temp, depth + 1)
            fish[temp] = shark_next
            arr[nx][ny], arr[x][y] = temp, -1


result = 0
temp = list(list(map(int, input().split())) for _ in range(4))
arr = [[0] * 4 for _ in range(4)]

fish = dict()
for i in range(4):
    for j in range(4):
        fish[temp[i][2 * j]] = (i, j, temp[i][2 * j + 1] - 1)
        arr[i][j] = temp[i][2 * j]

fish.pop(arr[0][0])
shark = (0, 0, temp[0][1]-1)
arr[0][0] = -1


dfs(arr, shark, fish, temp[0][0])
print(result)

