def f(i):
    if m == i:
        print(*ans)
    else:
        for j in range(1, n + 1):
            ans[i] = j
            f(i + 1)

n, m = map(int, input().split())
ans = [0] * m
f(0)
