import sys
input = sys.stdin.readline

n, k, q = map(int, input().split())
if k == 1:
    for _ in range(q):
        x, y = map(int, input().split())
        print(abs(x  - y))
else:
    for _ in range(q):
        x, y = map(int, input().split())
        x, y = x - 1, y - 1
        ans = 0
        while x != y:
            if x > y:
                if x %k == 0:
                    x -= 1
                x = x//k
                ans += 1
            else:
                if y%k == 0:
                    y -= 1
                y = y//k
                ans += 1

        print(ans)
