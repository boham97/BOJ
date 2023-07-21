N, K = map(int, input().split())
arr = []
for i in range(N):
    x, y = map(int,input().split())
    arr.append((x,y))


ans = 200001

def dfs(now, k, temp):
    global ans
    if k == K:
        maxd = 0
        for i in range(N):
            m = 200001
            for j in temp:
                m = min(m, abs(arr[i][0] -arr[j][0]) + abs(arr[i][1] - arr[j][1]))
            maxd = max(maxd, m)
        if maxd < ans:
            ans = maxd
        return
    for i in range(now + 1, N):
        temp.append(i)
        dfs(i, k + 1, temp)
        temp.pop()
dfs(-1, 0, [])
print(ans)
