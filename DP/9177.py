def check(i, j, k):
    global ans
    if i +j == k:
        ans = True
        return
    if dp[i][j]:
        return
    if i < len(a) and a[i] ==  c[i + j]:
        dp[i][j] = 1
        check(i+1, j, k)
    if j < len(b) and b[j] ==  c[i + j]:
        dp[i][j] = 1
        check(i, j + 1, k)
        
for i in range(1,  int(input()) + 1):
    a, b, c = input().split()
    ans = False
    dp = [[0] *(len(b) + 1) for _ in range(len(a) + 1)]
    check(0,0, len(c))
    print(f"Data set {i}: {'yes' if ans else 'no'}")
