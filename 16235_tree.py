from collections import deque
d = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
N, M, K = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(N)]
tree = [[deque() for _ in range(N)] for _ in range(N)]
field = [[5]* N for _ in range(N)]
for _ in range(M):
    x,y,z= map(int,input().split())
    tree[x-1][y-1].append(z)
year = 0
while year != K:
    for i in range(N):
        for j in range(N):
            temp = 0
            dead = 0
            for k in range(len(tree[i][j])):
                if field[i][j] >= tree[i][j][temp]:
                    field[i][j] -= tree[i][j][temp]
                    tree[i][j][temp] += 1
                    temp += 1
                else:
                    dead += (tree[i][j].pop())//2
            field[i][j] += dead

    for i in range(N):
        for j in range(N):
            for k in tree[i][j]:
                if k%5==0:
                    for l in range(8):
                        x =i+d[l][0]
                        y= j+d[l][1]
                        if 0 <= x <N and 0<=y<N:
                            tree[x][y].appendleft(1)
            field[i][j] += A[i][j]
    year += 1

ans =0
for i in range(N):
    for j in range(N):
        ans += len(tree[i][j])
print(ans)