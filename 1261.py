from collections import deque
import sys

input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

M, N = map(int, input().split())

arr = [list(map(int, list(input())[:-1])) for _ in range(N)]
visited = [[N*M]* M for _ in range(N)]

que = deque()
que.append((0,0))
visited[0][0] = 0


while que:
    x, y = que.popleft()
    time = visited[x][y]
    if x == N-1 and y == M -1:
        print(time)
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<= nx < N and 0<= ny < M:
            if arr[nx][ny] == 0 and visited[nx][ny] > time:
                visited[nx][ny] = time
                que.appendleft((nx,ny))

            elif arr[nx][ny] == 1 and visited[nx][ny] > time + 1:
                visited[nx][ny] = time + 1
                que.append((nx,ny))
            
