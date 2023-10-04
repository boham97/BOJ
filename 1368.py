import heapq

n = int(input())
w = list(int(input() )for _ in range(n))
arr = list(list(map(int ,input().split())) for _ in range(n))
road = []
for i in range(n):
    heapq.heappush(road, (w[i], i, i))
ans = 0
visit = [0] * n

cnt = 0
while road and cnt < n:
    cost, now, nxt = heapq.heappop(road)
    if visit[nxt]:
        continue
    ans += cost
    cnt += 1
    visit[nxt] = 1

    for i in range(n):
        heapq.heappush(road, (arr[nxt][i], nxt, i))
        
print(ans)
