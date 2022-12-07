from collections import deque
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0
biggest = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            que = deque()
            que.append([i,j])
            arr[i][j] = 0
            temp = 1
            ans += 1
            while que:
                x,y = que.popleft()
                for dx, dy in [[x+1,y],[x-1,y],[x,y+1],[x,y-1]]:
                    if 0<=dx<N and 0<=dy<M and arr[dx][dy] == 1:
                        arr[dx][dy] = 0
                        temp += 1
                        print(dx,dy, temp)
                        que.append([dx,dy])
            if temp > biggest:
                biggest = temp
print(ans)
print(biggest)