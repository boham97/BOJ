from collections import deque


N = int(input())
graph = [[] for _ in range(N+1)]
for i in range(N-1):
        num1, num2 = map(int,input().split())
        graph[num1].append(num2)
        graph[num2].append(num1)
used = [0] * (N+1)
que = deque()
que.append(1)
while que:
    node = que.popleft()
    for i in graph[node]:
        if used[i] == 0:
            que.append(i)
            used[i] = node
for i in range(2,N+1):
    print(used[i])
