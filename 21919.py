N =int(input())
arr = list(map(int, input().split()))

ans = 1
big = max(arr)
nums = [0] * (big + 1)

for i in range(2, big + 1):
    if nums[i] == 0:
        j = 2
        while j*i <= big:
            nums[j*i] = 1
            j += 1

for num in arr:
    if nums[num] == 0:
        ans *= num
        nums[num] = 1
if ans != 1:
    print(ans)
else:
    print(-1)
