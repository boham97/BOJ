from collections import deque

tc = int(input())
for test in range(tc):
    N, M, K = map(int,input().split())
    arr = [[0]* M for _ in range(N)]
    for _ in range(K):
        x, y = map(int,input().split())
        arr[x][y] = 1
    temp = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                arr[i][j] =0
                que = deque()
                que.append([i,j])
                temp += 1
                while que:
                    x,y = que.popleft()
                    for dx,dy in [[x+1,y],[x-1,y],[x,y+1],[x,y-1]]:
                        if 0<=dx<N and 0<=dy<M and arr[dx][dy]:
                            arr[dx][dy] = 0
                            que.append([dx,dy])
    print(temp)