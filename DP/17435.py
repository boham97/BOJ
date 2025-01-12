import sys
input = lambda : sys.stdin.readline().rstrip()
m = int(input())

dp = [[0] * (m + 1) for _ in range(20)]
dp[0] = list(map(int, input().split()))
dp[0].insert(0, 0)

for i in range(19):
    for j in range(m + 1):
        dp[i + 1][j] = dp[i][dp[i][j]]
    

for _ in range(int(input())):
    n, x = map(int, input().split())
    b = 19
    while n != 0:
        if n < 1<<b:
            b -= 1
            continue
        else:
            n -= 1<<b
            x = dp[b][x]
    print(x)

#2의 배수 만큼 미리 찾아둔다!
