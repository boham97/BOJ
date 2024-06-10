def cal_r():
    global R
    res_r = 0
    for i in range(C):
        res = [[0, j]for j in range(101)]
        for j in range(R):
            if arr[i][j] == 0:
                continue
            res[arr[i][j]][0] += 1

        res.sort()
        arr[i] = [0] * 100
        length = 0

        for j in range(101):
            if res[j][0] == 0 or length >= 100:
                continue
            arr[i][length] = res[j][1]
            arr[i][length + 1] = res[j][0]
            length += 2
        res_r = max(res_r, length)
    R = res_r

def cal_c():
    global C
    res_c = 0
    for i in range(R):
        res = [[0, j]for j in range(101)]
        for j in range(C):
            if arr[j][i] == 0:
                continue
            res[arr[j][i]][0] += 1
        res.sort()
        for j in range(100):
            arr[j][i] = 0
        length = 0
        for j in range(101):
            if res[j][0] == 0 or length >= 100:
                continue
            arr[length][i] = res[j][1]
            arr[length + 1][i] = res[j][0]
            length += 2
        res_c = max(res_c, length)
    C = res_c

def printAll():
    for i in range(C):
        print(arr[i][:R + 1])
    print()
r, c, k = map(int, input().split())

arr = list([0] * 100 for _ in range(100))
for i in range(3):
    arr[i][0], arr[i][1], arr[i][2] = map(int, input().split())
ans = 0
R, C = 3, 3
while arr[r - 1][c - 1] != k and ans <= 100:
    temp = cal_r() if R <= C else cal_c()
    ans += 1


print(ans if ans <= 100 else -1)
