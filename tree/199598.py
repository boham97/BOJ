from heapq import heappush, heappop

hq = [0]
n = int(input())
arr = [list(map(int ,input().split())) for _ in range(n)]
arr.sort()
for a, b in arr:
    if hq[0] <= a:
        heappop(hq)
    heappush(hq, b)
        
print(len(hq))
