import sys
input = sys.stdin.readline

from heapq import heappush, heappop

def find(i):
    while i != father[i]:
        i = father[i]
    return i

def union(i, j):
    i, j = find(i), find(j)
    if i != j:
        if i > j:
            i ,j = j, i
        father[j] = i
        return True
    return False


ans = 0
cnt = 0
n, c = map(int, input().split())
arr = list(list(map(int, input().split())) for _ in range(n))
hq = []
father = list( i for i in range(n))
for i in range(n):
    for j in range(i + 1, n):
        cost = (arr[i][0] - arr[j][0])**2 + (arr[i][1] - arr[j][1])**2
        if cost >= c:
            heappush(hq, (cost, i, j))

while hq and cnt < n -1 :
    cost, i, j = heappop(hq)
    logic = union(i,j)
    if logic:
        ans += cost
        cnt += 1

if cnt == n  -1:
    print(ans)
else:
    print(-1)
    
