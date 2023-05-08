from collections import deque

N, M = map(int, input().split())
arr = [[] for _ in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

ans = 0
temp = 5 * 1e6
for i in range(N):
    que = deque()
    que.append(i)
    visit = [5001] * (N+1)
    visit[i] = 1
    while que:
        n = que.popleft()
        now = visit[n]
        for next in arr[n]:
            if visit[next] > now + 1:
                visit[next] = now + 1
                que.append(next)
    if temp > sum(visit):
        temp = sum(visit)
        ans = i

print(ans)
