def f(i):
    if m == i:
        print(*ans)
    else:
        for j in range(1, n + 1):
            if visit[j]:
                continue
            visit[j] = 1
            ans[i] = j
            f(i + 1)
            visit[j] = 0

n, m = map(int, input().split())
ans = [0] * m
visit = [0] * (n + 1)
f(0)
