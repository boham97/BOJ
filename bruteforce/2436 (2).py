def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

X, Y = map(int, input().split())

ab = Y//X


for a in range(1, int(ab**0.5)+1):
    if ab%a:
        continue
    else:
        b = ab//a
        if gcd(a, b) == 1:
            res = (a,b)

print(a*X, b*X)
