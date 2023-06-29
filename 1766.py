import heapq
ans = []
N, M = map(int, input().split())
arr = [[] for _ in range(N +1)]
income = [0] * (N +1)
for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    income[b] += 1

hq = []
for i in range(1, N+1):
    if income[i] == 0:
        heapq.heappush(hq, i)

while hq:
    now = heapq.heappop(hq)
    ans.append(now)
    for i in arr[now]:
        income[i] -= 1
        if income[i] == 0:
            heapq.heappush(hq, i)
        
print(*ans)
