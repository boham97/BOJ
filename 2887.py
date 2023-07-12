from collections import deque
import sys

input = sys.stdin.readline

def find(node):
    if node == parent[node]:
        return node
    else:
        parent[node] = find(parent[node])
        return parent[node]


N = int(input())
arr = []
parent = [i for i in range(N)]
cnt = [1] * N
ans = 0
for i in range(N):
    x, y, z= map(int ,input().split())
    arr.append((i, x, y, z))

X = sorted(arr, key = lambda x: x[1])
Y = sorted(arr, key = lambda x: x[2])
Z = sorted(arr, key = lambda x: x[3])
temp = []
for i in range(N-1):
    temp.append((abs(X[i][1]-X[i+1][1]),X[i][0],X[i+1][0]))
    temp.append((abs(Y[i][2]-Y[i+1][2]),Y[i][0],Y[i+1][0]))
    temp.append((abs(Z[i][3]-Z[i+1][3]),Z[i][0],Z[i+1][0]))
temp.sort()
cost = deque(temp)

while cost:
    a, b, c = cost.popleft()
    bp = find(b)
    cp = find(c)
    if bp != cp:
        if cnt[cp] <  cnt[bp]:
            parent[cp] = bp
            
        else:
            parent[bp] = cp
            if cnt[bp] == cnt[cp]:
                cnt[cp] += 1
        ans += a

print(ans)
