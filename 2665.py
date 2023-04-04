import sys
from collections import deque

input = sys.stdin.readline
dx = [1,-1, 0 ,0]
dy = [0, 0, 1, -1]



N = int(input())

arr = list(list(map(int, list(input())[:-1])) for _ in range(N))

visited = [[N**2] * N for _ in range(N)]
visited[0][0] = 0
que = deque()
que.append((0,0))

while que:
    x,y = que.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<= nx < N and 0<= ny < N:
            if visited[nx][ny] > visited[x][y] + (1 - arr[nx][ny]):
                if arr[nx][ny]:
                    visited[nx][ny] = visited[x][y]
                    que.appendleft((nx,ny))
                    
                else:
                    visited[nx][ny] = visited[x][y]+1
                    que.append((nx, ny))

print(visited[N-1][N-1])
