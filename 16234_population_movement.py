dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

N, L, R = map(int, input().split())
nations = [list(map(int, input().split())) for _ in range(N)]
day = 0
while 1:
    ques = []
    arr = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(4):
                x = i + dx[k]
                y = j + dy[k]
                if 0 <= x < N and 0 <= y < N and L <= abs(nations[i][j]- nations[x][y]) <= R and arr[i][j] == 0 and arr[x][y] == 0:
                    que = [(x, y)]
                    ques.append([nations[x][y], 1])
                    arr[x][y] = len(ques)
                    while que:
                        x2, y2 = que.pop()
                        for n in range(4):
                            x = x2 + dx[n]
                            y = y2 + dy[n]
                            if 0 <= x < N and 0 <= y < N and L <= abs(nations[x2][y2]- nations[x][y]) <= R and arr[x][y] == 0:
                                que.append((x, y))
                                arr[x][y] = len(ques)
                                ques[-1][0] += nations[x][y]
                                ques[-1][1] += 1
    if len(ques) == 0:
        break
    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0:
                nations[i][j] = ques[arr[i][j]-1][0] // ques[arr[i][j]-1][1]
    day += 1


print(day)