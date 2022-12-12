N = int(input())
chu = list(map(int, input().split()))
M = int(input())
gushuls = list(map(int, input().split()))
K = 2*sum(chu)+1
h = sum(chu)
DP = [[0] * K for _ in range(N+1)]
DP[0][h] = 1
for i in range(N):
    for j in range(K):
        if DP[i][j]:
            DP[i+1][j] = 1
            if j +chu[i] < K:
                DP[i+1][j+chu[i]] = 1
            if j-chu[i] >= 0:
                DP[i+1][j-chu[i]] = 1

for gushul in gushuls:
    if gushul >h:
        print('N', end= ' ')
    elif DP[-1][h+gushul]:
        print('Y', end= ' ')
    else:
        print('N', end= ' ')
