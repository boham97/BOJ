import sys
from collections import deque

input = sys.stdin.readline
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
cnt = 1
while cnt:
    N = int(input())
    if N == 0:
        break

    arr = list(list(map(int, input().split())) for _ in range(N))

    visited = [[10*N*N] * N for _ in range(N)]

    que = deque()

    que.append((0,0))
    visited[0][0] = arr[0][0]

    while que:
        x, y, = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < N and 0<= ny < N and visited[nx][ny] > visited[x][y] + arr[nx][ny]:
                visited[nx][ny] = visited[x][y] + arr[nx][ny]
                que.append((nx, ny))
    print(f"Problem {cnt}: {visited[N-1][N-1]}")
    cnt += 1