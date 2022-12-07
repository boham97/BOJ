from collections import deque

while 1:
    L, R, C = map(int, input().split())
    if L == 0:
        break
    arr = []
    for _ in range(L):
        arr.append([list(input()) for _ in range(R)])
        temp = input()

    for i in range(L):
        for j in range(R):
            for k in range(C):
                if arr[i][j][k] =='S':
                    que = deque()
                    que.append([i,j,k,0])
                if arr[i][j][k] == 'E':
                    exit = [i,j,k]


    flag = 0
    while que :
        z,x,y,t = que.popleft()
        if exit[0]== z and  exit[1]==x and exit[2]==y:
            flag = 1
            break
        for dz,dx,dy in ([z+1,x,y],[z-1,x,y],[z,x+1,y],[z,x-1,y],[z,x,y+1],[z,x,y-1]):
            if 0<=dz<L and 0<=dx<R and 0<=dy<C and (arr[dz][dx][dy] =='.' or arr[dz][dx][dy] =='E'):
                arr[dz][dx][dy] ='S'
                que.append([dz,dx,dy,t+1])
    if flag:
        print(f'Escaped in {t} minute(s).')
    else:
        print('Trapped!')