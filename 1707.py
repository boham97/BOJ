from collections import deque
import sys

input = sys.stdin.readline

K = int(input())
for _ in range(K):
    V, E = map(int, input().split())
    arr = [[] for _ in range(V)]
    visit = [0] * (V)
    que = deque()
    ans = True
    for _ in range(E):
        a, b = map(int, input().split())
        arr[a-1].append(b-1)
        arr[b-1].append(a-1)
    for i in range(V):
        if visit[i] == 0:
            visit[i] = 1
            que.append(i)
            
            while que and ans:
                now = que.popleft()
                color = 1 + visit[now]%2
                for nxt in arr[now]:
                    if visit[nxt] == visit[now]:
                        ans = False
                        que = deque()
                    elif visit[nxt] == 0:
                        visit[nxt] = color
                        que.append(nxt)
        if ans == False:
            break
    print('YES' if ans else 'NO')
                        
        
