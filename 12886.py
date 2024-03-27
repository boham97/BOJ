from collections import deque

arr = list(map(int, input().split()))
arr.sort()
visit = [[0] * (1000) for _ in range(1000)]
visit[arr[0]][arr[2]] = 1
que = deque()
que.append((arr[0], arr[1], arr[2]))

while que:

    a, b, c = que.popleft()
    if a == c:
        print(1)
        break

    temp = [min(a+a, c-a), b, max(a+a, c-a)]
    temp.sort()
    na, nb, nc = temp[0], temp[1], temp[2]
    if visit[na][nb] == 0:
        visit[na][nb] = 1
        que.append((na, nb, nc))
        
    temp = [a, b+ b, c- b]
    temp.sort()
    na, nb, nc = temp[0], temp[1], temp[2]
    if visit[na][nb] == 0:
        visit[na][nb] = 1
        que.append((na, nb, nc))
    
else:
    print(0)
