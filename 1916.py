import heapq

N = int(input())
M = int(input())

arr = list({} for _ in range(N +1))

for _ in range(M):
    n, m , c = map(int, input().split())
    if m in arr[n]:
        arr[n][m] = min(arr[n][m], c)
    else:
        arr[n][m] = c


srt, end = map(int, input().split())


distance = [1e9] * (N+1)

que = []

que.append((0,srt))

while que:
    cost, node = heapq.heappop(que)
    if node == end:
        break

    for i, j in arr[node].items():
        if distance[i] > j + cost:
            distance[i] = j + cost
            heapq.heappush(que, (distance[i], i))

print(distance[end])