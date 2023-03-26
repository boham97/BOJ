from collections import deque

N = int(input())

arr = [0] * (N+1)
arr[N] = 0

que = deque()
que.append(N)

while que:
    now = que.popleft()
    if now == 1:
        break
    
    if not now%3 and arr[now//3] == 0:
        arr[now//3] = now
        que.append(now//3)
        
    if not now%2 and arr[now//2] == 0:
        arr[now//2] = now
        que.append(now//2)
        
    if arr[now -1] == 0:
        arr[now - 1] = now
        que.append(now-1)


ans = [1]

while ans[-1] != N:
    ans.append(arr[ans[-1]])
print(len(ans) - 1)
ans.reverse()
print(*ans)
