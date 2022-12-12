N,Q = map(int,input().split())
logic = dict()
arr = []
temp = [[0,0] for _ in range(N)]
for i in range(N): 
    x,y = map(int,input().split())
    temp[i][0] = x
    temp[i][1] = y
    logic[y] =1
for j in range(Q):
    q = input()

for i,j in arr:
    print(i)