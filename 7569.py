from collections import deque

M, N, H = map(int,input().split())
arr = [[list(map(int,input().split())) for _ in range(N)] for _ in range(H)]
que = deque()
logic = 0
ans = 0
for i in range(H):
    for j in range(N):
        for k in range(M):
            if arr[i][j][k] == 1:
                que.append([j,k,i,0])
            elif arr[i][j][k] == 0:
                logic += 1

while que:
    x,y,z,d = que.popleft()
    for dx, dy, dz in [[x+1,y,z],[x-1,y,z],[x,y-1,z],[x,y+1,z],[x,y,z+1],[x,y,z-1]]:
        if 0<=dx<N and 0<=dy<M and 0<=dz<H and arr[dz][dx][dy] == 0:
            arr[dz][dx][dy] = 1
            que.append([dx,dy,dz,d+1])
            logic -= 1
if logic == 0:
    print(d)
else:
    print(-1)