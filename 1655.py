from heapq import heappush, heappop

import sys
input = sys.stdin.readline

upper, lower = [], []

n = int(input())

for i in range(n):
    num = int(input())
    heappush(lower, -num)
    if i%2 == 1:
        heappush(upper, -heappop(lower))
        print (min(upper[0], -lower[0]))
    else:
        heappush(upper, -heappop(lower))
        heappush(lower, -heappop(upper))
        print(-lower[0])
