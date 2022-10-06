n,m = map(int,input().split())
ans = 1
temp = 1
for i in range(n-m,n):
    ans *= (i+1)
for i in range(1,m+1):
    temp *= i

print(ans//temp)