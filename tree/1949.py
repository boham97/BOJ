from sys import setrecursionlimit
setrecursionlimit(10**6)

def count(a):
    visit[a] = 1
    for i in grid[a]:
        if visit[i] == 0:
            count(i)
            dp[a][0] += dp[i][1]
            dp[a][1] += max(dp[i][0], dp[i][1])
    dp[a][0] += arr[a]
    visit[a] = 0

n = int(input())
arr = list(map(int, input().split()))
arr.insert(0, 0)
grid =[[] for _ in range(n + 1)]
dp = [[0, 0, 0] for _ in range(n + 1)]
visit = [0] * (n + 1)
for _ in range(n -1):
    a, b = map(int, input().split())
    grid[a].append(b)
    grid[b].append(a)

count(1)
print(max(dp[1]))
