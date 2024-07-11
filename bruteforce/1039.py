from collections import deque

def size(n):
    L = 0
    while n:
        n = n//10
        L += 1
    return L


def bfs(N):
    L = size(N)
    que = deque()
    que.append((N, 0))

    while que:
        n, k  = que.popleft()
        if k == K: continue
        for i in range(L):
            for j in range(i):
                if i == L - 1 and n// 10**j% 10 == 0: continue
                nextN = n + (n//10**i % 10 - n//10**j %10) * (- 10**i + 10**j)
                if k %2:
                    if nextN in even: continue
                    even.add(nextN)
                    que.append((nextN, k + 1))
                else:
                    if nextN in odd: continue
                    odd.add(nextN)
                    que.append((nextN, k + 1))    


N, K = map(int, input().split())

odd = set()
even = set()
odd.add(-1)
even.add(-1)
bfs(N)
print(max(odd) if K%2 else max(even))
