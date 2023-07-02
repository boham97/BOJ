from heapq import heappush, heappop

def find(node):
    if parent[node] != node:
        return find(parent[node])
    else:
        return node


def union(a, b):
    if a > b:
        parent[b] = a
    else:
        parent[a] = b


V, E = map(int, input().split())
parent = [i  for i in range(V+1)]

arr =[]
for _ in range(E):
    arr.append(list(map(int, input().split())))
arr.sort( key= lambda x : x[2])

ans = 0
for a, b, c in arr:
    pa, pb = find(a), find(b)
    if pa != pb:
        union(pa,pb)
        ans += c

print(ans)
