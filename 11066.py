import sys
from heapq import heappush, heappop, heapify
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    ans = 0
    k = int(input())
    hq = list(map(int, input().split()))
    heapify(hq)
    while len(hq)> 1:
        x, y = heappop(hq), heappop(hq)
        heappush(hq, x+y)
        ans += x + y
    print(ans)
