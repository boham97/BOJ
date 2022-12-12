from collections import deque
tc = int(input())
for test in range(tc):
    N = int(input())
    points = [list(map(int, input().split())) for _ in range(N+2)]
    arr = [[0] *(N+2) for _ in range(N+2)]
    for i in range(N+2):
        for j in range(N+2):
            arr[j][i] = arr[i][j] = abs(points[i][0]-points[j][0]) + abs(points[i][1]-points[j][1])
    que = deque()
    que.append(0)
    ans = 'sad'
    while que:
        x= que.popleft()
        if x == N+1:
            ans = 'happy'
            break
        for i in range(N+2):
            if 0 < arr[x][i] <= 1000:
                que.append(i)
                for j in range(N+2):
                    arr[j][i] = 0
    print(ans)