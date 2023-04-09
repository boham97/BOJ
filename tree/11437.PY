from collections import deque

n = int(input())
edge = [set() for _ in range(1+n)]
tree = [0] * (n + 1)
depth = [0] * (n +1)
for _ in range(n-1):
    a, b = map(int, input().split())
    edge[a].add(b)
    edge[b].add(a)


que = deque()
que.append(1)
visit = [1] * (1+n)
visit[1] = 0
while que:
    now = que.popleft()
    for next in edge[now]:
        if visit[next]:
            visit[next] = 0
            que.append(next)
            tree[next] = now
            depth[next] = depth[now] + 1


m = int(input())
for _ in range(m):
    a,b = map(int, input().split())

    while depth[a] != depth[b]:
        if depth[a] > depth[b]:
            a = tree[a]
        else:
            b= tree[b]
    while a != b:
        a, b = tree[a], tree[b]
    print(a)
