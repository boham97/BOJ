def cal(i, num):
    arr = cnt[i]
    arr[num] += 1
    first = 0
    for j in range(1,10):
        if arr[j] != 0:
            first = j
            break    
    arr[first] -= 1
    
    result = first
    for j in range(10):
        for k in range(arr[j]):
            result = result * 10 + j
    arr[num] -= 1
    arr[first] += 1
    return result
inf = 9999999999999999999999999999999999999999999999999999999999999999
cnt = [[0] * 10 for _ in range(101)]
dp = [inf] * 101
add = [6,2,5,5,4,5,6,3,7,6]
dp[2] = 1
dp[3] = 7
dp[4] = 4
dp[5] = 2
dp[6] = 0
dp[7] = 8
cnt[2][1] = 1
cnt[3][7] = 1
cnt[4][4] = 1
cnt[5][2] = 1
cnt[6][0] = 1
cnt[7][8] = 1

for i in range(2, 100):
    for j in range(2,8):
        if i+ j <= 100:
            temp_min = cal(i,dp[j])
            if 0 < temp_min < dp[i + j]:
                dp[i+j] = temp_min
                for k in range(10):
                    cnt[i+j][k] = cnt[i][k]
                cnt[i+j][dp[j]] += 1
            if j == 6:
                temp_min = cal(i, 6)
                if temp_min < dp[i + j]:
                    dp[i+j] = temp_min
                    for k in range(10):
                        cnt[i+j][k] = cnt[i][k]
                    cnt[i+j][6] += 1
dp[6] = 6

t= int(input())
for _ in range(t):
    n = int(input())
    ans = [0, 0]
    ans[0] = dp[n]
    temp = 0
    if n%2 == 1:
        temp = 7
    else:
        temp = 1
    n -= n%2 + 2
    while n:
        temp = temp * 10 + 1
        n -= 2
    ans[1] = temp
    print(*ans)
    

