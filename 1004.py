t = int(input())
for _ in range(t):
    x,y, x1, y1 = map(int,input().split())
    n = int(input())
    ans = 0
    for _ in range(n):
        a,b,d = map(int,input().split())
        if ((x-a)**2 + (y-b)**2 < d**2) != ((x1-a)**2 + (y1-b)**2 < d**2):
            ans += 1
    print(ans)
