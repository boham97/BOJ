from collections import deque
N, K = map(int, input().split())

que = deque(list(range(1,N+1)))

num = 0
ans = []
while que:
    x = que.popleft()
    num += 1
    if num == K:
        num = 0
        ans.append(x)
    else:
        que.append(x)

print('<', end='')
for x in ans:
    print(x, end='')
    if x != ans[-1]:
        print(end=', ')
print('>', end='')