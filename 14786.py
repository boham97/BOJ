import math
A, B, C = map(int, input().split())

left = min((C-B)/A, (C+B)/A)
right = max((C-B)/A, (C+B)/A)


def cal(x):
    return C - A*x - B*math.sin(x)

diff = 1

while abs(diff) > 0.0000001:
    mid = (left + right)/2
    diff = cal(mid)
    if diff > 0:
        left = mid
    else:
        right = mid
    print(mid)

print(mid)
