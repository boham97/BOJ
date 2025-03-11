import sys
sys.setrecursionlimit(5001)

def dfs(limit, node):
        for next_node, c in graph[node]:
            if c >= limit and visit[next_node] == 0:
                visit[next_node] = 1
                dfs(limit, next_node)


n, q = map(int, input().split())


graph = [[] for _ in range(n + 1)]
for i in range(1, n):
    a, b, c = map(int ,input().split())
    graph[a].append((b,c))
    graph[b].append((a, c))

for _ in range(q):
    a, b = map(int, input().split())
    visit =  [0] * (1 + n)
    visit[b] = 1
    dfs(a, b)
    print(sum(visit) - 1)
