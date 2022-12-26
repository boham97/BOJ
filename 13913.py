from collections import deque

N, K = map(int, input().split())
arr = [0] * 100001
time = [100003] * 100001
que = deque()
que.append(N)
time[N] = 0
while que:
    n = que.popleft()
    if n == K:
        break
    for i in [n - 1, n + 1, 2 * n]:
        if 0 <= i <= 100000 and time[i] > time[n] + 1:
            time[i] = time[n] + 1
            arr[i] = n
            que.append(i)

print(time[K])
num = K
ans = [K]
while num != N:
    ans.append(arr[num])
    num = arr[num]

print(*ans[::-1])