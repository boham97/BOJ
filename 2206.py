from collections import deque

N, M = map(int,input().split())
arr = [list(map(int,list(input()))) for _ in range(N)]
arr2 = [arr[i][:] for i in range(N)]
que = deque()
que.append([0,0])
arr[0][0] = 2
arr2[0][0] = 2
new_que = deque()
flag1 = 1
while que:
    x,y  = que.popleft()
    for dx,dy in [[x+1,y],[x-1,y],[x,y+1],[x,y-1]]:
        if 0<=dx<N and 0<=dy<M:
            if arr[dx][dy] ==0:
                arr[dx][dy] = arr[x][y]+1
                arr2[dx][dy] = arr[x][y]+1
                que.append([dx,dy])
            elif arr[dx][dy] == 1 and (arr2[dx][dy] == 1):
                arr2[dx][dy] = arr[x][y]+1
                new_que.append([dx,dy])
        if dx == N-1 and dy == M-1:
            flag1 = 0

flag2 = 1
while new_que:
    x,y  = new_que.popleft()
    for dx,dy in [[x+1,y],[x-1,y],[x,y+1],[x,y-1]]:
        if 0<=dx<N and 0<=dy<M:
            if (arr2[dx][dy] ==0 or arr2[dx][dy]>arr2[x][y]+1) and arr[dx][dy] != 1:
                arr2[dx][dy] = arr2[x][y]+1
                new_que.append([dx,dy])
        if dx == N-1 and dy == M-1:
            flag2 = 0

temp1 = arr[N-1][M-1]
temp2 = arr2[N-1][M-1]
if temp1 == 0 and temp2 == 0:
    print(-1)
elif min(temp1,temp2) != 0:
    print(min(temp1,temp2)-1)
else:
    print((temp1 or temp2)-1)