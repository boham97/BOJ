from collections import deque


arr =[100000] * 100001
N, K = map(int, input().split())
arr[N] = 0
que = deque()
que.append(N)
while que:
    now = que.popleft()
    if now-1 >= 0 and arr[now-1] > arr[now]+1:
        que.append(now-1)
        arr[now-1] = arr[now]+1
    if now+1 < 100001 and arr[now+1] > arr[now]+1:
        que.append(now+1)
        arr[now+1] = arr[now]+1
    if now*2 < 100001 and arr[now*2] > arr[now]:
        que.append(now*2)
        arr[now*2] = arr[now]
    if arr[K] != 100000:
        break
print(arr[K])