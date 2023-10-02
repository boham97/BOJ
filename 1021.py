from collections import deque

n, m = map(int, input().split())
q = deque()
for x in range(1, n+1):
    q.append(x)
arr = list(map(int, input().split()))
ans = 0
for i in arr:
    temp = 0
    while q[0] != i:
        q.append(q.popleft())
        temp += 1
    if temp < len(q) -temp:
        ans += temp
    else:
        ans += len(q) - temp
    q.popleft()

print(ans)
