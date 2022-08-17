import pprint

R, C, T = list(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(R)]

x = [-1, 1, 0, 0]
y = [0, 0, -1, 1]
direction = [0, 0 , 0, 0]
for i in range(R):
    if arr[i][0] == -1:
        up_cleaner = i +1
        down_cleaner = i + 2
        break
for i in range(R):
    arr[i].insert(0, -1)
    arr[i].append(-1)

arr.append([-1]*(C+2))
arr.insert(0, [-1]*(C+2))

t = 0
while t != T:
    mat = [[0]*(C+2) for _ in range(R+2)]

    for i in range(1,R+1):
        for j in range(1, C+1):
            if arr[i][j] != -1:
                cnt = 0 
                direction = [0, 0, 0, 0]
                for k in range(4):
                    if arr[i + x[k]][j + y[k]] != -1:
                        cnt += 1
                        direction[k] = 1
                for k in range(4):
                    if direction[k]:
                        mat[i + x[k]][j + y[k]] += int(arr[i][j] /5)
                mat[i][j] -= cnt * int(arr[i][j] /5)

    for i in range(1,R+1):
        for j in range(1, C+1):
            arr[i][j] += mat[i][j]

    for i in range(up_cleaner - 1, 1, -1):
        arr[i][1] = arr[i - 1][1]
    for i in range(1, C ):
        arr[1][i] = arr[1][i + 1]
    for i in range(1,up_cleaner):
        arr[i][C] = arr[i + 1][C]
    for i in range(C, 2, -1):
        arr[up_cleaner][i] = arr[up_cleaner][i - 1]
    arr[up_cleaner][2] = 0

    for i in range(down_cleaner + 1,R):
        arr[i][1] = arr[i + 1][1]
    for i in range(1, C ):
        arr[R][i] = arr[R][i + 1]
    for i in range(R,down_cleaner, -1):
        arr[i][C] = arr[i - 1][C]
    for i in range(C, 2, -1):
        arr[down_cleaner][i] = arr[down_cleaner][i - 1]
    arr[down_cleaner][2] = 0
    #pprint.pprint(arr)
    t += 1
ans = 0 
for i in range(1,R+1):
    for j in range(1, C+1):
        ans += arr[i][j]
print(ans+2)