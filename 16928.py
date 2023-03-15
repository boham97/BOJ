from collections import deque


ans = 10000
N, M = map(int, input().split())

ladder = [0] * 101
for i in range(N):
    n, m = map(int,input().split())
    ladder[n] = m
snake = [0] * 101
for i in range(M):
    n, m = map(int,input().split())
    snake[n] = m
    


visited = [10000] * 101
visited[1] = 0

que = deque()
que.append(1)

while que:
    now = que.pop()
    time = visited[now]
    if time > ans:
        continue
    elif now == 100:
        ans = time
        continue
    for i in range(1,7):
        next = now + i
        if next <= 100 and visited[next]> time + 1:
            visited[next] = time +1
            if ladder[next]:
                if visited[ladder[next]] > time + 1:
                    visited[ladder[next]] = time + 1
                    que.append(ladder[next])
            elif snake[next]:
                if visited[snake[next]] > time + 1:
                    visited[snake[next]] = time + 1
                    que.append(snake[next])
            else:
                que.append(next)

print(ans)
