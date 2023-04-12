import sys
sys.setrecursionlimit(150000)

input = sys.stdin.readline

def dfs(node):
    cnt[node] += 1
    for i in edge[node]:
        if cnt[i] == 0:
            cnt[node] += dfs(i)
    return cnt[node]


N, R, Q = map(int, input().split())

edge = [[] for _ in range(N+1)]
cnt = [0] * (N+1)

for _ in range(N-1):
    U, V = map(int, input().split())
    edge[U].append(V)
    edge[V].append(U)

dfs(R)

for _ in range(Q):
    now = int(input())
    print(cnt[now])
