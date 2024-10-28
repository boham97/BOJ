from collections import deque
t = int(input())

for _ in range(t):
    visit = [0] * 10000
    parent = [0] * 10000
    a, b = map(int ,input().split())
    visit[a] = 5
    que = deque()
    que.append(a)
    
    while que and not visit[b]:
        n = que.popleft()
        new = (2*n)%10000
        if not visit[new]:
            visit[new] = 'D'
            parent[new] = n
            que.append(new)
        new = n - 1
        if new == -1: new = 9999
        if not visit[new]:
            visit[new] = 'S'
            parent[new] = n
            que.append(new)
        new = (n%1000) * 10 + n//1000
        if not visit[new]:
            visit[new] = 'L'
            parent[new] = n
            que.append(new)
        new = (n//10) + 1000 * (n%10)
        if not visit[new]:
            visit[new] = 'R'
            parent[new] = n
            que.append(new)
    ans = deque()
    now = b
    while now != a:
        ans.append(visit[now])
        now = parent[now]
    while ans:
        print(ans.pop(), end= '')
    print()
