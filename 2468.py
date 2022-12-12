from collections import deque

delx = [-1,1,0,0]
dely = [0,0,1,-1]
N = int(input())
arr = [[] for _ in range(101)]
mat = [list(map(int, input().split())) for _ in range(N)]
highest = 0
ans = 1
for i in range(N):
    highest = max(mat[i]) if highest < max(mat[i]) else highest

for i in range(highest):
    copy_mat = [mat[n][:] for n in range(N)]
    temp = 0
    que = deque()
    for j in range(N):
        for k in range(N):
            if i>= copy_mat[j][k]:
                copy_mat[j][k] = 0
    for j in range(N):
        for k in range(N):
            if copy_mat[j][k]:
                que.append([j,k])
                temp += 1
                while que:
                    x, y = que.popleft()
                    for g in range(4):
                        dx = x + delx[g]
                        dy = y + dely[g]
                        if 0<= dx<N and 0<=dy<N and copy_mat[dx][dy]:
                            copy_mat[dx][dy] = 0
                            que.append([dx,dy])
    if temp > ans:
        ans = temp

print(ans)