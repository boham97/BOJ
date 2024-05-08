def check(i, j):
    if arr[i][j] != '.':
        return 0
    bit = 0
    if 0 <= i -1 and arr[i - 1][j] in ['|', '+', '1', '4', '7']:
        bit += 1
    if i + 1 < r and arr[i + 1][j] in ['|', '+', '2', '3', '5']:
        bit += 4
    if 0 <= j - 1 and arr[i][j - 1] in ['-', '+', '1', '2', '8']:
        bit += 8
    if j + 1< c and arr[i][j + 1] in ['-', '+', '3', '4', '6']:
        bit += 2    
    return bit

r, c = map(int, input().split())
arr = list(input().rstrip() for _ in range(r))
visit = [[0] * c for _ in range(r)]

ans = [0] * 16
ans[5] = '|'
ans[10] = '-'
ans[15] = '+'
ans[6] = '1'
ans[3] = '2'
ans[9] = '3'
ans[12] = '4'
point = ()
for i in range(r):
    for j in range(c):
        if arr[i][j] in ['M', 'Z']:
            bit = check(i,j)
            if bit == 1:
                arr[i][j] = '5'
            elif bit == 2:
                arr[i][j] = '6'
            elif bit ==4:
                arr[i][j] = '7'
            elif bit == 8:
                arr[i][j] = '8'

for i in range(r):
    for j in range(c):
        bit = check(i, j)
        if ans[bit] != 0:
            print(i + 1, j + 1, ans[bit])
            exit()
                
