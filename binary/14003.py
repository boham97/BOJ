from bisect import bisect_left

N = int(input())
arr = list(map(int, input().split()))

temp = [-1*1e10]
ans = []
L = 0
for num in arr:
  if num > temp[-1]:
    temp.append(num)
    ans.append(L)
    L += 1
  else:
    #temp[bisect_left(temp, num)] =num         #이진탐색

    start = 1
    end = len(temp)
    while start <= end:
        mid = (start + end)//2
        if temp[mid] >= num and temp[mid-1] < num:
            temp[mid] = num
            ans.append(mid-1)
            break
        elif temp[mid] < num:
            start = mid + 1
        elif temp[mid] > num:
            end = mid - 1

result = []
L -= 1
for i in range(N-1,-1,-1):          #배열 뒤에서 부터 넣을수 있는지 확인
    if ans[i] == L:                 #해당위치가 나왔으면 append
        result.append(arr[i])
        L -= 1                      #아래 자리로 내려간다 => 한번씩만 체크


print(len(result))
print(*result[::-1])