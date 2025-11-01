from collections import deque
import time
r, c = map(int, input().split())
grid = [list(input().strip()) for _ in range(r)]
visited = [[0] * c for _ in range(r)]
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
swan = deque()
ice = deque()

day = 0
start = None

for i in range(r):
    for j in range(c):
        if grid[i][j] == 'L':
            if start is None:
                start = (i,j)
            else:
                target = (i, j)
        if grid[i][j] == 'X':
            for k in range(4):
                di, dj = i + directions[k][0], j + directions[k][1]
                if 0 <= di < r and 0 <= dj < c and grid[di][dj] != 'X':
                    ice.append((i ,j, 0))
                    visited[i][j] = 1
                    break
                    
swan.append(start)
x, y = start
visited[x][y] = 2
print(start, target)

x, y = target
while 1:
    print(day)
    print(swan, ice)
    while swan:
        i, j = swan.popleft()
        for k in range(4):
            di, dj = i + directions[k][0], j + directions[k][1]
            if 0 <= di < r and 0 <= dj < c and grid[di][dj] != 'X' and visited[di][dj] != 2:
                swan.append((di ,dj))
                visited[di][dj] = 2

    if visited[x][y] == 2:
        print(day)
        break
    day += 1
    while ice:
        if ice[0][2] == day:
            print('break!', ice[0], day)
            break
        i, j, d = ice.popleft()
        grid[i][j] = '.'
        for k in range(4):
            di, dj = i + directions[k][0], j + directions[k][1]
            if 0 <= di < r and 0 <= dj < c:
                if grid[di][dj] == 'X' and visited[di][dj] == 0:
                    ice.append((di ,dj, d + 1))
                    visited[di][dj] = 1
                if visited[i][j] == 1 and visited[di][dj] == 2:
                    swan.append((i,j))
                    visited[i][j] = 2
    print(visited)
    print(grid)
    time.sleep(1)
    print()