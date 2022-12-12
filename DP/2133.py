ans = [0] * 31
ans[2] = 3
ans[0] = 1
N = int(input())
for i in range(4,N+1,2):
    ans[i] = ans[i-2] * 3
    for j in range(i-4,-1,-2):
        ans[i] += ans[j]*2

print(ans[N])