def find(i,num,M):
    if i == M:
        for j in range(N):
            if used[j]:
                print(arr[j],end=' ')
        print()
    else:
        for j in range(num,N-M+i+1):
            if used[j] == 0:
                used[j] = 1
                find(i+1,j,M)
                used[j] = 0
N, M = map(int,input().split())
arr = list(range(1,N+1))
arr.sort()
used = [0] * N
find(0,0,M)