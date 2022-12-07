from collections import deque
N, M = map(int,input().split())
que= deque()
que.append(N)
visited = [0] * 100001
visited[N] = 1
while que:
    x = que.popleft()
    if x == M:
        print(visited[M]-1)
        break
    for dx in [x-1,x+1,x*2]:
        if 0<=dx<=100000 and visited[dx]==0:
            visited[dx] =visited[x]+1
            que.append(dx)
