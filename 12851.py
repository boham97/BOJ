from collections import deque


arr =[100000] * 100001
time = [0] * 100001
N, K = map(int, input().split())
arr[N] = 0
que = deque()
que.append(N)
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