from collections import deque

A, B = map(int, input().split())

que = deque([(A,1)])

ans = -1

while que:
    now, cnt = que.popleft()
    if now == B:
        ans = cnt
        break

    if now * 2 <= B:
        que.append((now * 2, cnt + 1))

    if now * 10 + 1 <= B:
        que.append((now * 10 + 1, cnt + 1))

    
print(ans)