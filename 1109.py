from collections import deque
import pprint
N, M = map(int,input().split())
delx = [-1, -1, -1, 0, 0, 1,1,1]
dely = [-1,0,1,-1,1,-1,0,1]

delx2 = [-1, 1, 0, 0]
dely2 = [0, 0, 1, -1]

arr = [list(input()) for _ in range(N)]
arr.insert(0,['.']*(M+2))
arr.append(['.']*(M+2))
for i in range(1,N+1):
    arr[i].insert(0,'.')
    arr[i].append('.')

    
que = deque()
visit = [[1] * (M+2) for _ in range(N+2)]
hight = [[0] * (M+2) for _ in range(N+2)]



#섬 구분
temp = 0
for i in range(N+2):
    for j in range(M+2):
        if visit[i][j]:
            que.append((i,j))
            hight[i][j] = temp
            visit[i][j] = 0
            temp += 1
            while que:
                n, m = que.pop()
                if arr[n][m] == 'x':
                    for k in range(8):
                        dn = n + delx[k]
                        dm = m + dely[k]
                        if 0 <= dn < N+2 and 0 <= dm < M+2 and visit[dn][dm]:
                            if arr[n][m] == arr[dn][dm]:
                                que.appendleft((dn, dm))
                                visit[dn][dm] = 0
                                hight[dn][dm] = hight[n][m]
                else:
                    for k in range(4):
                        dn = n + delx2[k]
                        dm = m + dely2[k]
                        if 0 <= dn < N+2 and 0 <= dm < M+2 and visit[dn][dm]:
                            if arr[n][m] == arr[dn][dm]:
                                que.appendleft((dn, dm))
                                visit[dn][dm] = 0
                                hight[dn][dm] = hight[n][m]



parent = [0] * temp
land = [0] * temp

#트리 만들기
que.append((0,0))
visit[0][0] = 1
while que:
    n, m = que.popleft()
    if arr[n][m] == 'x':
        for i in range(8):
            dn = n + delx[i]
            dm = m + dely[i]
            if 0 <= dn < N+2 and 0 <= dm < M+2 and not visit[dn][dm]:
                if arr[dn][dm] == 'x':
                    que.appendleft((dn, dm))
                    visit[dn][dm] = 1
                else:
                    que.append((dn,dm))
                    visit[dn][dm] = 1
                    parent[hight[dn][dm]] = hight[n][m]
                
    else:
        for i in range(4):
            dn = n + delx2[i]
            dm = m + dely2[i]
            if 0 <= dn < N+2 and 0 <= dm < M+2 and not visit[dn][dm]:
                if arr[dn][dm] == '.':
                    que.appendleft((dn, dm))
                    visit[dn][dm] = 1
                else:
                    que.append((dn,dm))
                    visit[dn][dm] = 1
                    parent[hight[dn][dm]] = hight[n][m]
                    land[hight[dn][dm]] = 1
                
#자식 
son = [[] for _ in range(temp)]
for i in range(1, temp):
    if land[i]:
        son[parent[parent[i]]].append(i)


depth = [0] * temp
ans = [0] * temp
for i in range(temp):
    que.append((i, 0))
    while que:
        n, d = que.popleft()
        if d > depth[i]:
            depth[i] = d
        for k in son[n]:
            que.append((k, d +1))

for i in range(temp):
    if land[i]:
        ans[depth[i]] += 1
        
for i in range(temp):
    if ans[i] != 0:
        print(ans[i], end = ' ')
    else:
        break
if ans[0] == 0:
    print(-1)
