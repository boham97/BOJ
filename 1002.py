t = int(input())
for _ in range(t):
    x1, y1,r1,x2,y2, r2 = map(int, input().split())
    ans = 0
    distance = (x1-x2)**2 +(y1-y2)**2
    if distance in ((r2-r1)**2, (r2+r1)**2):
        if x1 == x2 and y1 == y2:
            ans = -1
        else:
            ans = 1
    elif (r2-r1)**2 < distance < (r2+r1)**2:
        ans =2
    print(ans)
