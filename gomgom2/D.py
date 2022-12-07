N = int(input())
arr = [list(input()) for _ in range(N)]
x = [N,0]
y = [N,0]
temp1 = 0
for i in range(N):
    if 'G' in arr[i]:
        temp1 += 1
    for j in range(N):
        if arr[i][j] == 'G':

            if j < x[0]:
                x[0] = j
            if j > x[1]:
                x[1] = j
            if i < y[0]:
                y[0] = i
            if i > y[1]:
                y[1] = i

ans = 0

if x[0] == x[1] and temp1 == 1:
    print(0)
elif x[0] == x[1] and temp1 != 1:
    ans += min(N-y[0]-1,y[1])
    print(ans)
elif x[0] != x[1] and temp1 == 1:
    ans += min(N-x[0]-1,x[1])
    print(ans)
else:
    ans += min(N-x[0]-1,x[1])
    ans += min(N-y[0]-1,y[1])
    print(ans)