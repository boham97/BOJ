from collections import deque
N, M = map(int,input().split())
arr =[list(map(int,list(input()))) for _ in range(N)]
que = deque()
que.append([0,0,1])
arr[0][0] = 0
while que:
    x,y,z = que.popleft()
    if x==N-1 and y==M-1:
        print(z)
        break
    for dx,dy in [[x+1,y],[x-1,y],[x,y+1],[x,y-1]]:
        if 0<=dx<N and 0<=dy<M and arr[dx][dy]:
            arr[dx][dy] = 0
            que.append([dx,dy,z+1])