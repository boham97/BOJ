from collections import deque

N, M = map(int, input().split())
arr = [[] for _ in range(N+1)]
index = [0] * (N + 1)


for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    index[b] += 1
    
temp = deque()
for i in range(1, N+1):
    if index[i] == 0:
        temp.append(i)
ans = []
while temp:
    now  = temp.popleft()
    ans.append(now)
    for i in arr[now]:
        index[i] -= 1
        if index[i] == 0:
            temp.append(i)

print(*ans)
    
