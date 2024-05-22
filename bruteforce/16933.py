from collections import deque
delta = [0, 0, 1, -1]
n, m , k = map(int, input().split())

arr = list(list(map(int, input().rstrip())) for _ in range(n))
que = deque()
que.append((0, 0, 0))
visit = [[k+1 for _ in range(m)] for _ in range(n)]
visit[0][0] = 0
ans = 1
day = True
while que:
    for _ in range(len(que)):
        x, y, z = que.popleft()
        if x == n - 1 and y == m-1:
            print(ans)
            exit()
        for i in range(4):
            dx = x + delta[i]
            dy = y + delta[3 - i]
            if 0 <= dx < n and 0 <= dy < m and visit[dx][dy] > z:
                if arr[dx][dy] == 0:
                    visit[dx][dy] = z
                    que.append((dx, dy, z))
                
                elif z < k:
                    if day:
                        visit[dx][dy] = z
                        que.append((dx, dy, z + 1))
                    else:
                        que.append((x, y, z))
    ans += 1
    day = not day
    
print(-1)
