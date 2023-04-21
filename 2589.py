from collections import deque
nx = [-1, 1, 0, 0]
ny = [0,0,1,-1]




N, M = map(int, input().split())
que = deque()
arr = [ input() for _ in range(N)]
ans = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'L':
            temp = 0
            for k in range(4):
                dx = i + nx[k]
                dy = j + ny[k]
                if 0 <= dx < N and 0 <= dy <M:
                    if arr[dx][dy] == 'W':
                        temp += 1
                else:
                    temp += 1
            if temp > 1:
                visit = [[0] *M for _ in range(N)]
                que.append((i,j))
                visit[i][j] = 1
                while que:
                    x, y = que.popleft()
                    for k in range(4):
                        dx = x + nx[k]
                        dy = y + ny[k]
                        if 0 <= dx < N and 0 <= dy <M and arr[dx][dy] == 'L' and visit[dx][dy] == 0:
                            que.append((dx,dy))
                            visit[dx][dy] = visit[x][y] + 1
                            if visit[x][y] +1 > ans:
                                ans = visit[x][y] + 1

print(ans-1)
