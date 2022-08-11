N, L = list(map(int, input().split()))
mat = [[] for _ in range(N)]
arr = [[] for _ in range(N)]
for i in range(N):
    mat[i] = list(map(int, input().split()))
    for j in range(N):
        arr[i].append(mat[i][j])
        arr[i].append(mat[i][j])
        arr[i].append(mat[i][j])

cnt = 0
for i in range(0, N):
    for j in range(0, N-L):
        for k in range(L):
            if arr[i][3*(j+k)+1] + 1 != arr[i][3*(j+L)+1]:
                break
        else:
            for k in range(L):
                arr[i][3 * (j + k)] += (3 * k) / (3 * L - 1)
                arr[i][3 * (j + k) + 1] += (3 * k + 1) / (3 * L - 1)
                arr[i][3 * (j + k) + 2] += (3 * k + 2) / (3 * L - 1)

        for k in range(L):
            if arr[i][3*(N-j-1-L) + 1] - 1 != arr[i][3*(N-j-1-k) + 1]:
                #print(i, j, k)
                break
        else:
            for k in range(L):
                arr[i][3 * (N - j - 1 - k)] += (3 * k + 2) / (3 * L - 1)
                arr[i][3 * (N - j - 1 - k) + 1] += (3 * k + 1) / (3 * L - 1)
                arr[i][3 * (N - j - 1 - k) + 2] += (3 * k + 0) / (3 * L - 1)

    for j in range(3*N-1):
        if abs(arr[i][j] - arr[i][j+1]) > 1/(3*L-1)*1.1:
            break
    else:
        cnt += 1

arr = [[] for _ in range(N)]
mat= list(zip(*mat))
for i in range(N):
    for j in range(N):
        arr[i].append(mat[i][j])
        arr[i].append(mat[i][j])
        arr[i].append(mat[i][j])


for i in range(0, N):
    for j in range(0, N - L):
        for k in range(L):
            if arr[i][3 * (j + k) + 1] + 1 != arr[i][3 * (j + L) + 1]:
                break
        else:
            for k in range(L):
                arr[i][3 * (j + k)] += (3 * k) / (3 * L - 1)
                arr[i][3 * (j + k) + 1] += (3 * k + 1) / (3 * L - 1)
                arr[i][3 * (j + k) + 2] += (3 * k + 2) / (3 * L - 1)

        for k in range(L):
            if arr[i][3 * (N - j - 1 - L) + 1] - 1 != arr[i][3 * (N - j - 1 - k) + 1]:
                # print(i, j, k)
                break
        else:
            for k in range(L):
                arr[i][3 * (N - j - 1 - k)] += (3 * k + 2) / (3 * L - 1)
                arr[i][3 * (N - j - 1 - k) + 1] += (3 * k + 1) / (3 * L - 1)
                arr[i][3 * (N - j - 1 - k) + 2] += (3 * k + 0) / (3 * L - 1)

    for j in range(3 * N - 1):
        if abs(arr[i][j] - arr[i][j + 1]) > 1 / (3 * L - 1) * 1.1:
            break
    else:
        cnt += 1

print(cnt)
