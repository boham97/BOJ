arr = [[0]*101 for _ in range(101)]
ans = 0

case = int(input())
for square in range(case):
    x1, y1 = map(int,input().split())
    for x in range(x1,x1+10):
        for y in range(y1,y1+10):
            if arr[x][y] == 0:
                ans += 1
                arr[x][y] = 1
print(ans)
            