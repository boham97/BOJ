from collections import deque
from pprint import pprint
tc = int(input())
for test in range(tc):
    delta = [[1,0],[-1,0],[0,1],[0,-1]]
    M, N = map(int,input().split())
    arr = [list(input()) for _ in range(N)]
    que = deque()
    flag = 1
    for i in range(N):
        for j in range(M):
            if arr[i][j] == '*':
                que.append([i,j,'*',0])
    for i in range(N):
        for j in range(M):
            if arr[i][j] == '@':
                que.append([i,j,'@',0])
                break
    while que and flag:
        x, y, z,t = que.popleft()
        if z =='@' and (x ==0 or x== N-1 or y == 0 or y == M-1):
            flag = 0
            break
        else:
            for d1,d2 in delta:
                dx = x + d1
                dy = y + d2
                if 0<=dx<N and 0<=dy<M and ((z=='@' and arr[dx][dy] == '.')or(z=='*' and (arr[dx][dy]=='.' or arr[dx][dy]=='@'))):
                    arr[dx][dy] = z
                    que.append([dx,dy,z,t+1])

    if not flag:
        print(t+1)
    else:
        print('IMPOSSIBLE')
