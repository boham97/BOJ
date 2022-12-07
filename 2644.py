N = int(input())
X, Y = map(int, input().split())
M = int(input())
arr = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    x,y = map(int, input().split())
    arr[x][y] = 1
    arr[y][x] = 1

stack = [X]
visit = [0] *(N+1)
visit[X] = 0
while stack and not visit[Y]:
    x = stack[-1]
    for i in range(N+1):
        if arr[x][i] and not visit[i]:
            visit[i] = visit[x]+1
            stack.append(i)
            break
    else:
        stack.pop()
print(visit[Y]) if visit[Y] else print(-1)