from heapq import heappush, heappop
n = int(input())
arr = list(list(map(int, input().split())) for _ in range(n))
arr.sort(key = lambda x: x[1])
res = 0
ans = []
for a, b,c in arr:
    if ans and ans[0] <= b:
        heappop(ans)
    heappush(ans, (c))
    if res < len(ans):
        res = len(ans)
print(res)
        
