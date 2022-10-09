from collections import deque


arr =[100001] * 100001
N, K = map(int, input().split())
arr[N] = 0
que = deque()
que.append(N)
ans = 1
while que:
    now = que.popleft()
    for num in [now-1,now+1,now*2]:
        if 0<= num < 100001 and arr[num] > arr[now]+ 1:
                que.append(num)
                arr[num] = arr[now]+ 1
        if num == K and arr[K] == arr[now] + 1:
            ans += 1
print(arr[K])
print(ans)


"""     if now-1 >= 0 and arr[0][now-1] > arr[0][now]+1:
        que.append(now-1)
        arr[0][now-1] = arr[0][now]+1
    if now+1 < 100001 and arr[0][now+1] > arr[0][now]+1:
        que.append(now+1)
        arr[0][now+1] = arr[0][now]+1
    if now*2 < 100001 and arr[0][now*2] > arr[0][now]:
        que.append(now*2)
        arr[0][now*2] = arr[0][now]
    if arr[K] != 100000:
        break
print(arr[K]) """