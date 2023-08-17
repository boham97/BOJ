import sys
from heapq import heappush, heappop
input = sys.stdin.readline
arr = []
bags = []
N, K = map(int, input().split())
for _ in range(N):
    temp = list(map(int,input().split()))
    arr.append(temp)
arr.sort()

for _ in range(K):
    bags.append(int(input()))
bags.sort()

ans =0
j = 0
hq = []
for i in range(K):
    value = 0
    while j < N and bags[i]>= arr[j][0]:
        heappush(hq, -arr[j][1])
        j += 1
    if hq:
        ans -= heappop(hq)
print(ans)
