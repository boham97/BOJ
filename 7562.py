from collections import deque

tc = int(input())
for test in range(tc):
    N = int(input())
    x, y = map(int, input().split())
    xend, yend = map(int, input().split())
    visited = [[0]*N for _ in range(N)]
    que = deque()
    que.append((x, y, 0))
    while que:
        x,y,z = que.popleft()
        if x==xend and y== yend:
            print(z)
            break
        for dx,dy in [[x-2,y-1],[x-2,y+1],[x-1,y-2],[x-1,y+2],[x+1,y-2],[x+1,y+2],[x+2,y-1],[x+2,y+1]]:
            if 0<=dx<N and 0<= dy<N and visited[dx][dy] == 0:
                visited[dx][dy] = 1
                que.append([dx,dy,z+1])