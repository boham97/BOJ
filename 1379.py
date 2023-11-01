import sys
from heapq import heappush, heappop

input = sys.stdin.readline
n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
lecture = [0] * (n + 1)
arr.sort(key=lambda x: x[1])
room = [i for i in range(1, n+ 1)]

hq = []
for x in arr:
    if hq and hq[0][0] <= x[1]:
        end, r = heappop(hq)
        heappush(room, r) #입력 후보로 
    r = heappop(room)
    heappush(hq, [x[2], r])
    lecture[x[0]] = r
    
print(max(lecture))
for x in lecture[1:]:
    print(x)
