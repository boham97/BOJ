arr = [list(map(int, input().split())) for _ in range(9)]

ans = -1
x, y = 0,0
for i in range(9):
    for j in range(9):
        if arr[i][j] > ans:
            ans, x, y = arr[i][j], i+1,j+1

print(ans)
print(x,y)