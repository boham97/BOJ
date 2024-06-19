n = int(input())

arr = [[[
        [0] * 11 for _ in range(11)]
         for _ in range(11)]
       for _ in range(n + 1)]

for i in range(1,10):
    arr[1][i][i][i] = 1
# 자리수 최대값 최소값 마지막값
for i in range(n):
    for j in range(10):
        for k in range(10):
            for m in range(10):
                arr[i + 1][max(j, m + 1)][k][m + 1] += arr[i][j][k][m]
                arr[i + 1][j][min(k, max(m - 1, 0))][m - 1] += arr[i][j][k][m]
        
ans = 0
for i in range(10):
    ans += arr[n][9][0][i]

print(ans % 1000000000)
            

