A, B, C = map(int,input().split())
a, b, c = map(int,input().split())
ans = 0

if a>=A:
    ans += A
    a -= A
    b += a//3
    A = 0
    a = a%3
else:
    ans += a
    A -= a
    a = 0

if b>=B:
    ans += B
    b -= B
    c += b//3
    B = 0
    b = b%3
else:
    ans += b
    B -= b
    b = 0

if c>=C:
    ans += C
    c -= C
    a = c//3
    C = 0
    c = c%3
else:
    ans += c
    C -= a
    c = 0


if a>=A:
    ans += A
    a -= A
    b += a//3
    A = 0
    a = a%3
else:
    ans += a
    A -= a
    a = 0

if b>=B:
    ans += B
    b -= B
    c += b//3
    B = 0
    b = b%3
else:
    ans += b
    B -= b
    b = 0

if c>=C:
    ans += C
    c -= C
    a = c//3
    C = 0
    c = c%3
else:
    ans += c
    C -= a
    c = 0
print(ans)