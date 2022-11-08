dlt = [[-1, 0], [1, 0], [0, 1], [0, -1]]
N, M = map(int, input().split())
cnt = 0
arr = [list(map(int, input().split())) for _ in range(N)]
DP = [[0] * M for _ in range(N)]
DP[N-1][M-1] = 1
stack = [[0, 0, -1]]
flag = 0
while stack:
    x, y, z = stack[-1]
    if flag:
        flag = 0
        z = temp
    else:
        z = -1
    for i in range(z+1, 4):
        dx, dy = x+dlt[i][0], y+dlt[i][1]
        if 0 <= dx < N and 0 <= dy < M and arr[x][y] > arr[dx][dy] and DP[dx][dy] != -1:
            if DP[dx][dy] == 0:
                stack.append([dx, dy, i])
                break
            if DP[dx][dy] > 0:
                for x, y, z in stack:
                    DP[x][y] += DP[dx][dy]
                #print(x, y, stack)
                cnt += DP[dx][dy]
    else:
        flag = 1
        if DP[x][y] == 0:
            DP[x][y] = -1
        temp1, temp2, temp = stack.pop()
#print(DP)
print(cnt)

'''
못가는 길이면 pop 했을떄 DP[x][y] == 0 => DP[x][y] = -1 로 변경
-1이면 안가서 경우의수 줄이기
'''