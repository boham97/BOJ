from bisect import bisect_left

N = int(input())
arr = list(map(int, input().split()))

ans = [0,1000000]

for num in arr:
  if num > ans[-1]:
    ans.append(num)
  else:
    #ans[bisect_left(ans, num)] =num         #이진탐색

    start = 1
    end = len(ans)
    while start <= end:
        mid = (start + end)//2
        if ans[mid] >= num and ans[mid-1] < num:
            ans[mid] = num
            break
        elif ans[mid] < num:
            start = mid + 1
        elif ans[mid] > num:
            end = mid - 1

print(len(ans)-1)
