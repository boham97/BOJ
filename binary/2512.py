N = int(input())
arr = list(map(int, input().split()))
M = int(input())
start = 0
end = max(arr)
ans = 0
while start <= end:
    mid = (start + end) // 2
    temp = 0
    for budget in arr:
        if budget <= mid:
            temp += budget
        else:
            temp += mid
    if temp > M:
        end = mid - 1
    else:
        if mid > ans:
            ans = mid
        start = mid + 1


print(ans)
