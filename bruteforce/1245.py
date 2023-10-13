from collections import deque
def bfs(i,j):
    logic = True
    visit[i][j] = 0
    que.append((i,j))
    while que:
        x, y = que.popleft()
        for k in range(8):
            dx, dy = x + delta[k][0], y + delta[k][1]
            if 0<= dx < n and 0<=dy < m:
                if arr[dx][dy] == arr[i][j] and visit[dx][dy]:
                    que.append((dx,dy))
                    visit[dx][dy] = 0
                elif arr[dx][dy] > arr[i][j]:
                    logic = False
    return logic


n, m = map(int, input().split())

arr = list(list(map(int, input().split())) for _ in range(n))
visit = [[1] * m for _ in range(n)]
delta = [[-1, -1] , [-1,0], [-1,1],[0,-1,],[0,1], [1,-1], [1,0], [1,1]]
ans = 0
que =deque()

for i in range(n):
    for j in range(m):
        if visit[i][j] and arr[i][j] and bfs(i,j):
            ans+=1

print(ans)
        
