N = int(input())

arr = list( [0] * 5 for  _ in range(N))
for i in range(5):
    arr[0][i] = 1
    
for i in range(1, N):
    for j in range(1,5):
        for k in range(1,5):
            if abs(j-k) > 1:
                arr[i][j] += arr[i-1][k]
        arr[i][0] += arr[i-1][j]
        arr[i][0] %= 1000000007
        
        arr[i][j] += arr[i-1] [0]
        arr[i][j] %= 1000000007
        
ans  = 0
for i in range(5):
    ans += arr[N-1][i]
    ans %= 1000000007

print(ans)
