from collections import deque
N, M, V = map(int,input().split())
arr = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    x,y = map(int, input().split())
    arr[x][y] = 1
    arr[y][x] = 1

stack = [V]
ans2 = [V]
while stack:
    x = stack[-1]
    for i in range(N+1):
        if arr[x][i] and i not in ans2:
            stack.append(i)
            ans2.append(i)
            break
    else:
        stack.pop()

que = deque()
que.append(V)
ans = [V]
while(que):
    x = que.popleft()
    for i in range(N+1):
        if arr[x][i] and i not in ans:
            que.append(i)
            ans.append(i)
print(*ans2)
print(*ans)