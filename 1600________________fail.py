from collections import deque
delta = [[1,0],[-1,0],[0,1],[0,-1]]
horse = [[-2,-1],[-2,1],[-1,-2],[-1,2],[1,-2],[1,2],[2,-1],[2,1]]
K = int(input())
M, N = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
que = deque()
arr[0][0] = K+2
que.append([0, 0, 2, K+2])
ans = 50000
while que:
    x,y,z,h = que.popleft()
    if x==N-1 and y==M-1:
        if ans > z:
            ans = z
    for i in range(4):
        dx, dy = x+delta[i][0], y+delta[i][1]
        if 0<=dx<N and 0<=dy<M and arr[dx][dy] <h and arr[dx][dy] != 1:
            que.append([dx,dy,z+1,h])
            arr[dx][dy] = h
    for i in range(8):
        dx, dy = x+horse[i][0], y + horse[i][1]
        if 0<=dx<N and 0<=dy<M  and arr[dx][dy] <h and arr[dx][dy] != 1 and arr[x][y]>2:
            que.append([dx,dy,z+1,h-1])
            arr[dx][dy] = h-1
"""     print(arr[0])
    print(arr[1])
    print(arr[2])
    print(arr[3])
    print() """
if ans == 50000:
    print(-1)
else:
    print(ans-2)