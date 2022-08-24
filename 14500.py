case = []
for m in range(3):
    for n in range(3):
        if m != n and m!=1 and n!=1:
            mat= [[1,1,1],[1,1,1]]
            mat[0][m] = 0
            mat[1][n] = 0
            case.append(mat)

            if m > n :
                mat= [[1,1,1],[1,1,1]]
                mat[0][m] = 0
                mat[0][n] = 0
                case.append(mat)

                mat= [[1,1,1],[1,1,1]]
                mat[1][m] = 0
                mat[1][n] = 0
                case.append(mat)

        elif m!= n and m>n:
            mat= [[1,1,1],[1,1,1]]
            mat[0][m] = 0
            mat[0][n] = 0

            mat= [[1,1,1],[1,1,1]]
            mat[1][m] = 0
            mat[1][n] = 0
            case.append(mat)
case2 =[]
for arr in case:
    temp = [[0]*2 for _ in range(3)]
    for i in range(3):
        for j in range(2):
            temp[i][j] = arr[j][i]
    case2.append(temp)
print(case2)