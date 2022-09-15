dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1,-1, 0, 1]
N, M, K = map(int,input().split())
energy = [list(map(int,input().split())) for _ in range(N)]
tree = [list(map(int,input().split())) for _ in range(M)]
arr = [[5]* N for i in range(N)]
tree.sort()             #좌표순, 나이순
i = 0
while i < M:
    tree[i][0], tree[i][1]= tree[i][0]-1, tree[i][1]-1
    i += 1
for year in range(K):
    i = 0
    temp = []
    while i < M:
        x,y, age = tree[i][0], tree[i][1], tree[i][2]  #spring
        if age <= arr[x][y]:
            arr[x][y] -= age
            tree[i][2] += 1
            i += 1
        else:
            temp.append(tree.pop(i))
            M-= 1
    for x,y,age in temp:
        arr[x][y] += age//2

    j = 0
    while j < M:                                 #autumn
        x, y, age = tree[j][0], tree[j][1], tree[j][2]
        if age % 5 == 0:
            for i in range(8):
                if 0 <= x+dx[i] < N and 0 <= y+dy[i] < N:
                    tree.insert(0,[x+dx[i], y+dy[i], 1])
                    M += 1
                    j += 1
            j+= 1
        else:
            j += 1
    for i in range(N):
        for j in range(N):
            arr[i][j] += energy[i][j]
    #print(len(tree))
    print(arr)
