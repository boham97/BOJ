n,m = map(int, input().split())
a  = list(list(input()) for _ in range(n))
b  = list(list(input()) for _ in range(n))

ans = 0
for i in range(n - 2):
    for j in range(m - 2):
        if a[i][j] == b[i][j]:
            continue
        ans += 1
        for r in range(3):
            for t in range(3):
                if b[i + r][j + t] == '0':
                    b[i + r][j + t] = '1'
                else:
                    b[i + r][j + t] = '0'

print(ans if a == b else -1)
