import math, sys

input= sys.stdin.readline
X = 1000000007

def func(x, y):
    return y * devide(x, X-2) % X

def devide(n, i):
    if i == 1:
        return n
    elif i % 2 == 0:
        return devide(n, i//2) ** 2 % X
    else:
        return n *devide(n, i-1) % X
    
M = int(input())
ans = 0

for _ in range(M):
    x,y = map(int, input().split())
    num = math.gcd(x,y)
    x //= num
    y //= num

    ans = (ans + func(x,y)) % X


print(ans)