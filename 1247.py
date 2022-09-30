def dfs(i,expect):
    global ans
    if expect > ans:
        return
    if i == N+1:
        expect = expect-short[arr[i-1]] + graph[arr[i-1]][1]
        if expect < ans:
            ans = expect
        return
    else:
        for j in range(i,N+1):
            arr[i], arr[j] = arr[j], arr[i]
            dfs(i+1,expect-short[arr[i-1]]+graph[arr[i-1]][arr[i]])
            arr[i], arr[j] = arr[j], arr[i]
tc = int(input())
for test in range(tc):
    N = int(input())
    ans = 200 * 12
    point = list(map(int,input().split()))
    arr = list(range(N+2))
    arr.pop(1)                                      


    graph = [[0]*(N+2) for _ in range(N+2)]
    for i in range(N+2):
        for j in range(N+2):
            if i == j:
                graph[i][j] = 110
            else:
                graph[i][j] = abs(point[2*i]- point[2*j])+abs(point[2*i+1]- point[2*j+1])

    short = [0] * (N+2)
    for i in range(N+2):
        short[i] = min(graph[i])
    dfs(1,sum(short)-short[1])
    print(f'#{test+1} {ans}')
