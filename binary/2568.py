from sys import stdin
input = stdin.readline

n = int(input())
arr = list(list(map(int, input().split())) for _ in range(n))
arr.append([0, 0])
arr.sort()

temp = [-1]

for i in range(n + 1):
    num = arr[i][1]

    if num == 0:
        continue
    if num > temp[-1]:
        temp.append(num)


    else:
        start = 1
        end = len(temp)
        while start <= end:
            mid = (start + end)// 2
            if temp[mid] >= num and temp[mid-1] < num:
                temp[mid] = num
                break
            elif temp[mid] < num:
                start = mid + 1
            elif temp[mid] > num:
                end = mid - 1

j = len(temp) - 1
temp.append(5000001)
i = n
ans = []
while i > 0:
    if j >0 and temp[j] <= arr[i][1] <= temp[j + 1]:
        j -= 1
    else:
        ans.append(arr[i][0])
    i -= 1
ans.sort()
print(len(ans))
for i in ans:
    print(i)
