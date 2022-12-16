from bisect import bisect_left

N = int(input())
arr = list(map(int, input().split()))

ans = [0, 1000001]


for num in arr:
    if num> ans[-1]:
        ans.append(num)
    else:
        index = bisect_left(ans, num)
        ans[index] = num


print(N-len(ans)+1)
