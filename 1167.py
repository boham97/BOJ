import sys
sys.setrecursionlimit(100001)
input = sys.stdin.readline

def dfs(now):
    global ans
    global maxnode
    
    for nextnum, cost in edge[now]:
        if visit[nextnum] == 0:
            visit[nextnum] = visit[now] + cost
            if visit[nextnum] > ans:
                maxnode = nextnum
                ans = visit[nextnum]
            dfs(nextnum)


V = int(input())
ans = 0
maxnode = 0
edge = [[] for _ in range(V + 1)]
visit = [0]  * (V + 1)
visit[1] = 1

for _ in range(V):
    temp = list(map(int, input().split()))
    for i in range(1, len(temp)-2, 2):
        edge[temp[0]].append((temp[i],temp[i+1]))


dfs(1)

visit = [0] * (V+1)
visit[maxnode] = 1
dfs(maxnode)
print(ans -1 )
