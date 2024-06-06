from collections import deque
from sys import stdin
input = stdin.readline

delta = [[0, 0, 1, -1], [1, -1, 0, 0]]
def check(di, dj):
    global ans
    if arr[di][dj] == '*':
        return
    elif arr[di][dj] == '.':
        que.append((di, dj))
    elif 'a' <= arr[di][dj] <= 'z':
        key = ord(arr[di][dj]) - ord('a')
        keys[key] = 1
        que.append((di, dj))
        for door_i, door_j in doors[key]:
            if visit[door_i][door_j]:
                que.append((door_i, door_j))
    elif 'A' <= arr[di][dj] <= 'Z':
        if keys[ord(arr[di][dj]) - ord('A')]:
                que.append((di, dj))
    else:
        ans += 1
        que.append((di, dj))
    visit[di][dj] = 1

        
for _ in range(int(input())):
    ans = 0
    x, y = map(int, input().split())
    arr = [list(input().rstrip()) for _ in range(x)]
    keys = [0] * 26
    doors = [[] for _ in range(26)]
    visit = [[0] * y for _ in range(x)]
    
    #find door position
    keyInput = list(input().rstrip())
    if keyInput[0] != '0':
        for c in keyInput:
            keys[ord(c) - ord('a')] = 1
            
    for i in range(x):
        for j in range(y):
            if 'A' <= arr[i][j] <= 'Z':
                door = ord(arr[i][j]) - ord('A')
                doors[door].append((i,j))
                
    #queue init
    que = deque()
    for i in range(x):
        check(i, 0)
        check(i, y - 1)
    #모서리에 문서가 있으면 중복으로 ans += 1 됩니다 
    for i in range(1, y - 1):
        check(0, i)
        check(x - 1, i)
            
    while que:
        i, j = que.popleft()
        for k in range(4):
            di, dj = i + delta[0][k], j + delta[1][k]
            if 0 <= di < x and 0 <= dj < y and visit[di][dj] == 0:
                check(di, dj)
                
    print(ans)



















                    
