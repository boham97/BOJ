from collections import deque

N =int(input())
arr = [list(map(int, list(input()))) for _ in range(N)]

ans = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            que = deque()
            que.append([i,j])
            temp = 1
            arr[i][j] = 0
            while que:
                x, y = que.popleft()
                for dx, dy in([x+1,y],[x-1,y],[x,y+1],[x,y-1]):
                    if 0<=dx<N and 0<=dy<N and arr[dx][dy]:
                        arr[dx][dy] = 0
                        temp += 1
                        que.append([dx,dy])
            ans.append(temp)

ans.sort()
print(len(ans))
for num in ans:
    print(num)