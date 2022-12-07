from collections import deque

N, M = map(int, input().split())
delta = [[1,0],[-1,0],[0,1],[0,-1]]
arr = [list(map(int, input().split())) for _ in range(N)]
que = deque()
bing =deque()
ice = 0
for i in range(N):
    for j in range(M):
        if not arr[i][j]:
            for k in range(4):
                di = i + delta[k][0]
                dj = j + delta[k][1]
                if 0<=di<N and 0<=dj<M and arr[di][dj]:
                    que.append([i,j,0])
                    break
        else:
            ice += arr[i][j]
temp = -1



while ice and que:
    x,y,z = que.popleft()
    if temp != z:
        temp = z
        bing.clear()
        visited = [[0]*M for _ in range(N)]
        num = 0
        for i in range(N):
            for j in range(M):
                if visited[i][j]==0 and arr[i][j]:
                    num +=1
                    bing.append([i,j])
                    visited[i][j] = num
                    
                    while bing:
                        x2,y2 = bing.popleft()
                        for k in range(4):
                            dx2 = x2 + delta[k][0]
                            dy2 = y2 + delta[k][1]
                            if 0<=dx2<N and 0<=dy2<M and arr[dx2][dy2] and visited[dx2][dy2] == 0:
                                bing.append([dx2,dy2])
                                visited[dx2][dy2] = num
        if num > 1:
            print(temp)
            break
    flag = 0
    for k in range(4):
        dx = x + delta[k][0]
        dy = y + delta[k][1]
        if 0<=dx<N and 0<=dy<M and arr[dx][dy]:
            arr[dx][dy] -= 1
            ice -= 1
            flag = 1
            if arr[dx][dy] == 0:
                que.append([dx,dy,z+1])
    if flag:
        que.append([x,y,z+1])


if ice == 0:
    print(0)
