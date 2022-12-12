A, B = map(int, input().split())

x = 1
temp1 = 0
while x<A:
    x = x<<1

while x >= 1:
    temp1 += x*(A//(2*x))
    if (A//x)%2 == 1:
        temp1 += A%x
    x = x>>1

B += 1
x = 1
temp2 = 0
while x<B:
    x = x<<1

while x >= 1:
    temp2 += x*(B//(2*x))
    if (B//x)%2 == 1:
        temp2 += B%x
    x = x>>1

print(temp2-temp1)