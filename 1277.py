from heapq import heappush, heappop
import sys
input = sys.stdin.readline
def func_cost(i, j):
    return ((arr[i][0] - arr[j][0])**2 + (arr[i][1] - arr[j][1])**2)**0.5

n, w = map(int, input().split())
m = float(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
distance = [100000000] * n
distance[0] = 0
graph = [[100000000] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        temp = func_cost(i,j)
        if temp <= m:
            graph[i][j] = temp

for _ in range(w):
    a, b, = map(int, input().split())
    graph[a - 1][b - 1] = 0
    graph[b - 1][a - 1] = 0

hq = []
hq.append((0,0))
while hq:
    cost, i = heappop(hq)
    for j in range(n):
        if distance[i] + graph[i][j] < distance[j]:
            distance[j] = distance[i] + graph[i][j]
            heappush(hq, (graph[i][j], j))
print(int(distance[-1] *1000))
