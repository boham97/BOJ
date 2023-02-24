from collections import deque
N, M = map(int, input().split())
arr = list(dict() for _ in range(N+1))
for _ in range(M):
    A, B, C = map(int, input().split())
    """ 다리가 여러개있을수있어서 채크 필요 """
    if B in arr[A]:
        if arr[A][B] < C:
            arr[A][B] = C
            arr[B][A] = C
    else:
        arr[A][B] = C
        arr[B][A] = C
    
go, to = map(int, input().split())

que = deque()
que.append(go)
visited = [-1] * (N + 1)
visited[go] = 1000000001 

while que:
    now = que.popleft()
    if visited[now] > visited[to] and visited:
        for i in arr[now]:
            value = min(arr[now][i], visited[now])
            if visited[i] < value:
                visited[i] = value
                que.append(i)


print(visited[to])