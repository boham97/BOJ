from itertools import combinations


tc = int(input())
for test in range(tc):
    N = int(input())
    arr = []
    xsum = 0
    ysum = 0

    for _ in range(N):
        x, y = map(int, input().split())
        arr.append((x,y))
        xsum += x
        ysum += y
    ans = 1e20

    for array in combinations(list(range(N)), N//2):
        X, Y = xsum, ysum
        for i in array:
            X -= 2 * arr[i][0]
            Y -= 2 * arr[i][1]
        temp = (X**2 + Y**2)
        if temp < ans:
            ans = temp
    print(ans**0.5)