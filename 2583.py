from collections import deque

N, M , K = map(int,input().split())
arr = [[0]*M for _ in range(N)]
for _ in range(K):
    y1, x1, y2, x2 = map(int, input().split())
    for x in range(x1,x2):
        for y in range(y1,y2):
            arr[x][y] = 1

ans = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            que = deque()
            que.append([i,j])
            temp = 1
            arr[i][j] = 1
            while que:
                x, y = que.popleft()
                for dx, dy in([x+1,y],[x-1,y],[x,y+1],[x,y-1]):
                    if 0<=dx<N and 0<=dy<M and arr[dx][dy] == 0:
                        arr[dx][dy] = 1
                        temp += 1
                        que.append([dx,dy])
            ans.append(temp)

print(len(ans))
ans.sort()
print(*ans)