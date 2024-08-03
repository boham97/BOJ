n = int(input())
arr = list(map(int, input().split()))
res = [0]
pos = []
index = 0
for num in arr:
    if res[-1] < num:
        pos.append(index)
        index += 1
        res.append(num)
        continue
    
    left, right = 1, len(res) - 1
    mid = (left + right)//2
    while left <= right:
        if res[mid - 1] < num <= res[mid]:
            res[mid] = num
            pos.append(mid - 1)
            break
        elif res[mid] > num: right = mid - 1
        elif res[mid] < num: left = mid + 1

ans = []
for i in range(n - 1, - 1, -1):
    if pos[i] == index:
        ans.append(arr[i])
        index -= 1
print(len(ans))
print(*ans[::-1])