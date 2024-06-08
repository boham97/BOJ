from collections import deque
from sys import stdin
input = stdin.readline

def magic():
    d, s = map(int, input().split())
    change = range(1)
    if d == 1:
        for i in range(n//2 - 1, max(0, n//2 - s) - 1, -1):
            arr[i][n//2] = 0
    elif d == 2:
        for i in range(n//2 + 1, min(n, n//2 + s + 1)):
            arr[i][n//2] = 0
    elif d == 3:
        for i in range(n//2 - 1, max(0, n//2 - s) - 1, -1):
            arr[n//2][i] = 0
    else:
        for i in range(n//2 + 1, min(n, n//2 + s + 1)):
            arr[n//2][i] = 0

delta = [[0, 1, 0, -1], [1, 0, -1, 0]]

def streak():
    temp = 0
    i, j = 0, 0
    que = deque()
    last = 4
    multi = 0
    zero = 0
    d = 0
    end_i, end_j = n//2, n//2
    visit = [[0] *n for _ in range(n)]
    visit[0][0] = 1
    while i != end_i or j != end_j:
        if arr[i][j] == 0:
            zero += 1
        else:
            if last != arr[i][j]:
                que.append([multi, last])
                last = arr[i][j]
                multi = 1
            else:
                multi += 1
        di = i + delta[0][d]
        dj = j + delta[1][d]
        if 0 <= di < n and 0<= dj < n and visit[di][dj] == 0:
            pass
        else:
            d = (d +1) %4
        i += delta[0][d]
        j += delta[1][d]
        visit[i][j] = 1
    que.append([multi, last])

    change = True
    while change:
        change = False
        for i in range(len(que)):
            multi, now = que.popleft()
            if multi > 3:
                zero += multi
                temp += multi * now
                change = True
            elif que and que[-1][1] == now:
                que[-1][0] += multi
            else:
                que.append([multi, now])
                
    que.popleft()
    new = deque([0] * (n * n - 1))
    size = n *n - 1
    while que:
        a, b, = que.popleft()
        new.append(b)
        new.append(a)
        new.popleft()
        new.popleft()

        
    i, j = 0, 0
    d = 0
    last = 0
    end_i, end_j = n//2, n//2
    visit[0][0] = 0
    while i != end_i or j != end_j:

        arr[i][j] = new.popleft()
            
        di = i + delta[0][d]
        dj = j + delta[1][d]
        if 0 <= di < n and 0<= dj < n and visit[di][dj] == 1:
            pass
        else:
            d = (d +1) %4
        i += delta[0][d]
        j += delta[1][d]
        visit[i][j] = 0

    
    return temp

def printAll():
    for i in range(n):
        print(arr[i])

ans = 0
n, m = map(int, input().split())
arr = list(list(map(int, input().split())) for _ in range(n))

for _ in range(m):
    magic()
    ans += streak()
print(ans)
