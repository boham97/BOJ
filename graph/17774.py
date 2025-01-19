def find(x):
    while x != parent[x][0]:
        x = parent[x][0]
    return x

def union(x, y):
    px, py = find(x), find(y)
    if px != py:
        if px > py:
            parent[px][0] = py
        else:
            parent[py][0] = px
        return 1
    else:
        return 0

def distance(i, j):
    dx = abs(parent[i][1] - parent[j][1])
    dy = abs(parent[i][2] - parent[j][2])
    return (dx**2 + dy**2, i, j)
    
import sys
from heapq import heappush, heappop
from decimal import Decimal

input = lambda : sys.stdin.readline().rstrip()
cnt = 0

n, m = map(int, input().split())
parent = [ [i, 0, 0] for i in range(n + 1)]
for i in range(1, n + 1):
    x, y = map(int, input().split())
    parent[i][1], parent[i][2] = x, y
    
for _ in range(m):
    a, b = map(int, input().split())
    if union(a, b):
        cnt += 1


ans = 0
h = []
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j: continue
        heappush(h, (distance(i, j)))


while h:
    a, b, c = heappop(h)
    if union(b, c):
        ans += a**0.5
        cnt += 1
    if cnt == n -1:
        break
print(f"{ans:.2f}")
