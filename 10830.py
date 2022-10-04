def gob(cnt):
    if cnt in memo:
        return memo[cnt]
    elif cnt%2 ==0:
        y = gob(cnt//2)
        temp = [[0]*N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                for k in range(N):
                    temp[i][j] += y[i][k] * y[k][j]
                temp[i][j] %= 1000
        memo[cnt] = list(temp[i][:] for i in range(N))
        return temp
    else:
        y = gob((cnt-1)//2)
        temp = [[0]*N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                for k in range(N):
                    temp[i][j] += y[i][k] * y[k][j]
                temp[i][j] %= 1000
        memo[cnt-1] = list(temp[i][:] for i in range(N))
        y = gob((cnt-1))
        temp = [[0]*N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                for k in range(N):
                    temp[i][j] += y[i][k] * arr[k][j]
                temp[i][j] %= 1000
        memo[cnt] = list(temp[i][:] for i in range(N))
        return temp



N,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
for i in range(N):
    for j in range(N):
        arr[i][j] %= 1000
memo = {
    1: arr,
}
ans = gob(M)
for i in range(N):
    print(*ans[i])