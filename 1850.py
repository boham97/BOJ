A, B = map(int, input().split())

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

for i in range(gcd(A,B)):
    print("1", end = '')
print()
