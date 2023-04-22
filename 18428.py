from itertools import permutations

N = int(input())
arr = [ list(input().split()) for _ in range(N)]
deltax = [-1,1,0,0]
deltay = [0,0,1,-1]

student = []
wall = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 'S':
            student.append((i,j))
        if arr[i][j] == 'X':
            wall.append((i,j))
            

for test in permutations(wall, 3):
    for x, y in test:
        arr[x][y] = 'O'
    logic = 1
    for i, j in student:
        for k in range(4):
                di = i 
                dj = j
                while 1:
                    di += deltax[k]
                    dj += deltay[k]
                    if 0<= di < N and 0<= dj < N:
                        if arr[di][dj] == 'O':
                            break
                        elif arr[di][dj] == 'T':
                            logic = 0
                            break
                    else:
                        break
    for x, y in test:
        arr[x][y] = 'O'
    if logic == 1:
        break

    
if logic:
    print("YES")
else:
    print("NO")
