case1 = [
    [[1,1,0],[0,1,1]],
    [[0,1,1],[1,1,0]],
    [[0,1,0],[1,1,1]],
    [[1,1,1],[0,1,0]],
    [[1,1,1],[1,0,0]],
    [[1,1,1],[0,0,1]],
    [[1,0,0],[1,1,1]],
    [[0,0,1],[1,1,1]],
]
case2 = [
    [[1,0],[1,1],[0,1]],
    [[0,1],[1,1],[1,0]],
    [[0,1],[1,1],[0,1]],
    [[1,0],[1,1],[1,0]],
    [[1,1],[1,0],[1,0]],
    [[1,0],[1,0],[1,1]],
    [[1,1],[0,1],[0,1]],
    [[0,1],[0,1],[1,1]],
]
case3 = [
    [[1,1],[1,1]]
]
case4 = [
    [[1,1,1,1],[]]
]
case5 = [
    [[1],[1],[1],[1]]
]
case= [case1, case2, case3, case4, case5]
size = [[2,3],[3,2],[2,2],[1,4],[4,1]]
N, M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
max_hab = 0 # 최대합
for i in range(5):
    for j in case[i]:
        for x in range(N-size[i][0]+1):
            for y in range(M-size[i][1]+1):
                hab = 0
                for x2 in range(size[i][0]):
                    for y2 in range(size[i][1]):
                        hab += j[x2][y2]*arr[x+x2][y+y2]
                if hab >  max_hab:
                    max_hab = hab
print(max_hab)