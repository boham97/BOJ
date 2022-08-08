import itertools

mat_num, chick = list(map(int,input().split()))
home = []
chicken = []
mat = [[] for _ in range(mat_num)]
for i in range(mat_num):
    mat[i] = list(map(int,input().split()))
    for j in range(mat_num):
        if mat[i][j] == 1:
            home.append([i, j])
        elif mat[i][j] == 2:
            chicken.append([i,j])
chick_road = [[0 for _ in range(chick)] for i in range(len(home))]
mincnt = 10000
for chickhouse in itertools.combinations(range(len(chicken)),chick):
    #print(chickhouse)
    cnt = 0 
    for i in range(len(home)):
        for j in range(chick):
            chick_road[i][j] = abs(home[i][0] - chicken[chickhouse[j]][0]) + abs(home[i][1] - chicken[chickhouse[j]][1])
        cnt += min(chick_road[i])
    if cnt < mincnt:
        mincnt = cnt
print(mincnt)
