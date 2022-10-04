A, B, C = map(int,input().split())
ans = 0
temp = 1
while B>1:
    for i in range(1,B+1):
        if A**i > C:
            break
    temp = max((temp *A**(B%i))%C,1)
    A = (A**i)%C
    B = B//i
print((A*temp)%C)