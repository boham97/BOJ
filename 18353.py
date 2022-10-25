'''
N = int(input())
arr = list(map(int, input().split()))
ans = [1] * N

for i in range(N):
    for j in range(i-1,-1,-1):
        if arr[i] < arr[j]:
            ans[i] = ans[j]+1
            break
    print(ans)
print(N-max(ans))
'''

N = int(input())
arr = list(map(int, input().split()))
ans = [1] * N

for i in range(N):
    for j in range(i):
        if arr[i] < arr[j]:
            ans[i] = max(ans[i], ans[j]+1)

print(N-max(ans))
