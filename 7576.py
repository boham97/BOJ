from collections import deque
M, N = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
que = deque()
cnt  = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            que.append([i,j,0])
        elif arr[i][j] == 0:
            cnt += 1

while que:
    x,y,day = que.popleft()
    for dx,dy in [[x+1,y],[x-1,y],[x,y+1],[x,y-1]]:
        if 0<=dx<N and 0<=dy<M and arr[dx][dy] ==0:
            cnt -= 1
            arr[dx][dy] =1
            que.append([dx,dy,day+1])
if cnt ==0:
    print(day)
else:
    print(-1)
