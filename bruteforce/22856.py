import sys
sys.setrecursionlimit(100000)

def dfs(i):
    global ans
    left = arr[i][0]
    right = arr[i][1]
    if visit[i]:
        return
    print(i)
    visit[i] = 1
    ans += 1
    dfs(left)
    dfs(right)
    ans += 1
    
n = int(input())
arr = list([0] * (2) for _ in range(n + 1))
visit = [0] * (n + 1)
ans = 0
res = 0
for _ in range(n):
    a, b, c = map(int, input().split())
    arr[a][0] = max(b, 0)
    arr[a][1] = max(c, 0)

visit[0] = 1
dfs(1)
