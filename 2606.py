N = int(input())
M = int(input())
arr = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    x,y = map(int,input().split())
    arr[x][y] = 1
    arr[y][x] = 1

stack = [1]
visit = [1] *(N+1)
visit[1] = 0
while stack:
    x = stack[-1]
    for i in range(N+1):
        if arr[x][i] and visit[i]:
            visit[i] = 0
            stack.append(i)
            break
    else:
        stack.pop()

print(N-sum(visit))