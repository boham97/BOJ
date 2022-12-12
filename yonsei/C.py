N, M = map(int,input().split())
arr = list(map(int,input().split()))
hab = [0] * (N+1)
for i in range(N):
    hab[i+1] = hab[i] +arr[i] 
ans = 0
i =0
j = 1
#print(hab)
while i < N and j <N+1:
    temp = hab[j] -hab[i]
    if temp <= M:
        if ans < temp:
            ans = temp
        j += 1
    else:
        i += 1
print(ans)