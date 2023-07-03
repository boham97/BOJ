import sys

N, S = map(int, input().split())
arr = list(map(int, sys.stdin.readline().split()))

left = 0
temp = 0
ans = 1000000

for i in range(N):
    temp += arr[i]
    while temp >= S:
        if ans > (i - left + 1):
            ans = i - left + 1
        temp -= arr[left]
        left += 1
if ans == 1000000:
    print(0)
else:
    print(ans)
    
