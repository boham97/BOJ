N, M, T = list(map(int,input().split()))

arr = [[] for _ in range(N)]
for i in range(N):
    arr[i] = list(map(int, input().split()))

order_arr = []
for t in range(T):
    order_arr.append(list(map(int, input().split())))

for turn in range(T):
    r, cw, time = order_arr[turn][:]
    for i in range(r-1, N, r):
        for j in range((1 - cw)*(time % M)+cw*(M - time % M)):
            temp = arr[i].pop()
            arr[i].insert(0, temp)
    change = list()
    for i in range(N):
        for j in range(M):
            if arr[i][j] == arr[i][j - 1] and arr[i][j] != 0:
                change.append([i, j])
                change.append([i, j - 1])
            if arr[i][j] == arr[i - 1][j] and i > 0 and arr[i][j] != 0:
                change.append([i, j])
                change.append([i - 1, j])

    for pos in change:
        arr[pos[0]][pos[1]] = 0
    if len(change) == 0:
        cnt = 0
        avg = 0
        for i in range(N):
            for j in range(M):
                if arr[i][j] != 0:
                    avg += arr[i][j]
                    cnt += 1
        if cnt != 0:
            avg = avg / cnt
            for i in range(N):
                for j in range(M):
                    if arr[i][j] != 0:
                        if arr[i][j] > avg:
                            arr[i][j] -= 1
                        elif arr[i][j] < avg:
                            arr[i][j] += 1
ans = 0
for i in range(N):
    ans += sum(arr[i])
print(ans)