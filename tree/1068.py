from collections import deque

N = int(input())

tree = list(map(int, input().split()))
cut = int(input())

son = [[] for _ in range(N)]
start = -1
for i in range(N):
    if tree[i] != -1:
        son[tree[i]].append(i)
    else:
        start = i
    
      


ans = 0
que = deque()
que.append(start)


while que:
    now = que.popleft()
    if now == cut:
        continue
    
    if son[now] == [] or [cut]:
        ans += 1
    else:
        for next in son[now]:
            que.append(next)

print(ans)
