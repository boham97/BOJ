from collections import deque


<<<<<<< HEAD
arr =[100001] * 100001
=======
arr =[100000] * 100001
time = [0] * 100001
>>>>>>> ba140444107e26e3fa75a12b44a4e8e936c7c0ee
N, K = map(int, input().split())
arr[N] = 0
que = deque()
que.append(N)
<<<<<<< HEAD
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
=======
ans = 0
while que:
    now = que.popleft()
    for num in [now-1,now+1,now*2]:
        if 0 <= num < 100001:
            if arr[num] > arr[now]+1:
                que.append(num)
                arr[num] = arr[now]+1
                if num == K:
                    ans = 0
            elif arr[num] == arr[now]+1:
                que.append(num)
                arr[num] = arr[now]+1
        if K == num and arr[num] == arr[now]+1:
            ans += 1

print(arr[K])
if N != K:
    print(ans)
else:
    print(1)
>>>>>>> ba140444107e26e3fa75a12b44a4e8e936c7c0ee
