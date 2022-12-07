N,L = map(int,input().split())
xx = list(map(int,input().split()))
ww = list(map(int,input().split()))

temp1 = 0
temp2 = 0
for i in range(N):
    temp1 += xx[i]*ww[i]
    temp2 += ww[i]

print(temp1/temp2)