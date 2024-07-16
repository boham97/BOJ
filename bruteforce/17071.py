from collections import deque

N, k = map(int, input().split())
odd = [0] * 500001
even = [0] * 500001
even[N] = 1
que = deque()
que.append((N, 0))

while que:
    n, t = que.popleft()
    kt = k + t * (t + 1)//2
    if kt > 500000:
        continue
    #print(n, t, kt)
    if odd[kt] if t%2 else even[kt]:
        print(t)
        break
    if 2 * n <= 500000:
        if t%2 and  even[2 * n] == 0:
            even[2 * n] = 1
            que.append((2 * n, t + 1))
        elif t%2 == 0 and odd[2 * n] == 0:
            odd[2 * n] = 1
            que.append((2 * n, t + 1))
    if n + 1 <= 500000:
        if t%2 and  even[n + 1] == 0:
            even[n + 1] = 1
            que.append((n + 1, t + 1))
        elif t%2 == 0 and odd[n + 1] == 0:
            odd[n + 1] = 1
            que.append((n + 1, t + 1))
    if n - 1 >= 0:
        if t%2 and  even[n - 1] == 0:
            even[n - 1] = 1
            que.append((n - 1, t + 1))
        elif t%2 == 0 and odd[n - 1] == 0:
            odd[n - 1] = 1
            que.append((n - 1, t + 1))
else:
    print(-1)
