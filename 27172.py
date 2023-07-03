import sys

input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
sets = set(nums)
maxnum = max(nums)
arr = [0] * (maxnum+1)

for i in nums:
    j = 2
    while i*j <= maxnum:
        if i*j in sets:
            arr[i*j] -= 1
            arr[i] += 1
        j += 1
        
ans = [0] * N
for i in range(N):
    ans[i] = arr[nums[i]]

print(*ans)
