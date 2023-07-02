N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

dp = [[[1000000] *3 for _ in range(N)] for _ in range(3)]


dp[0][0][0] = arr[0][0]
dp[1][0][1] = arr[0][1]
dp[2][0][2] = arr[0][2]

for i in range(3):
    for j in range(1,N):
        for k in range(3):
            temp = 1000001
            target = 0
            for b in range(3):
                if k != b:
                    if temp > dp[i][j-1][b]:
                        temp = dp[i][j-1][b]
                        target = b
            dp[i][j][k] = dp[i][j-1][target] + arr[j][k]


ans = 1000001
for i in range(3):
    for j in range(3):
        if i != j and dp[i][N-1][j] < ans:
            ans = dp[i][N-1][j]

print(ans)
