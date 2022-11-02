arr = [[0]*102 for _ in range(102)]
N = int(input())
for _ in range(N):
    x, y = map(int,input().split())
    x += 1
    y += 1
    for i in range(x,x+10):
        for j in range(y, y+10):
            arr[i][j] = 1
drt = [[-1,0], [1,0], [0,1], [0,-1]]
ans = 0
for x in range(1,101):
    for y in range(1,101):
        for k in range(4):
            dx = x+drt[k][0]
            dy = y+drt[k][1]
            if arr[x][y] == 1 and arr[dx][dy] ==0 :
                ans += 1

print(ans)