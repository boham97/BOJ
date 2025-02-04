from heapq import heappush, heappop

def find(x):
    while x != par[x]:
        x = par[x]
    return x

    
n = int(input())
ans = 0
cnt = 1
q = []
par = [i for i in range(n)]
pos = []
for _ in range(n):
    pos.append(list(map(float, input().split())))

for i in range(n):
    for j in range(i + 1, n):
        dx = pos[i][0] - pos[j][0]
        dy = pos[i][1] - pos[j][1]
        heappush(q, ((dx * dx + dy * dy) **0.5, i, j))

while cnt != n  and q:
    cost, x, y = heappop(q)
    px, py = find(x), find(y)
    if px == py: continue
    par[max(px, py)] = min(px, py)
    ans += cost
    cnt += 1

print( round(ans, 2))

