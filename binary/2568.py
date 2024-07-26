from sys import stdin
input = stdin.readline

n = int(input())
arr = list(list(map(int, input().split())) for _ in range(n))
arr.append([0, 0])
arr.sort()

temp = [-1]
dp = [1]
ans = []

for i in range(n + 1):
    num = arr[i][1]

    if num == 0:
        continue
    if num > temp[-1]:
        temp.append(num)
        dp.append(len(temp) - 1)

    else:
        start = 1
        end = len(temp)
        while start <= end:
            mid = (start + end)// 2
            if temp[mid] >= num and temp[mid-1] < num:
                temp[mid] = num
                dp.append(mid)
                break
            elif temp[mid] < num:
                start = mid + 1
            elif temp[mid] > num:
                end = mid - 1

L = len(temp) - 1
for i in range(n , 0, -1):
    if dp[i] == L:
        L -= 1
    else:
        ans.append(arr[i][0])
ans.reverse()
print(len(ans))
print(*ans, sep='\n')
