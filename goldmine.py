tc = int(input())
for test in range(tc):
    N, M = map(int,input().split())
    temp = list(map(int,input().split()))
    arr = [[0] * M for _ in range(N)]
    ans = [[0] * M for _ in range(N)]
    for i in range(N*M):
        arr[i//M][i%M] = temp[i]
    for i in range(M):
        for j in range(N):
            if not i:
                ans[j][i] = arr[j][i]
            else:
                temp = 0
                for k in range(-1,2):
                    if N>j+k>= 0:
                        if ans[j+k][i-1] > temp:
                            temp = ans[j+k][i-1]
                ans[j][i] = temp + arr[j][i]
    result = 0
    for i in range(N):
        if ans[i][-1] > result:
            result = ans[i][-1]
    print(result)
