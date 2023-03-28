from bisect import bisect_left


n = int(input())

arr = list(map(int, input().split()))
visited = [0] * n
leng = [1]

ans = [1001]

for i in range(n):
    num = arr[i]
    if num > ans[-1]:
        ans.append(num)
        visited[i] = num
        leng.append(leng[-1]+1)
    else:
        if bisect_left(ans, num) == len(ans)-1:
            visited[i] = num
        else:
            visited[i] = visited[i-1]
        ans[bisect_left(ans, num)] = num
        leng.append(leng[-1])

leng= leng[1::]


visited2 = [0] * n
leng2 = [1]

arr = arr[::-1]
ans = [1001]

for i in range(n):
    num = arr[i]
    if num > ans[-1]:
        ans.append(num)
        visited2[i] = num
        leng2.append(leng2[-1]+1)
    else:
        if bisect_left(ans, num) == len(ans)-1:
            visited2[i] = num
        else:
            visited2[i] = visited2[i-1]
        ans[bisect_left(ans, num)] = num
        leng2.append(leng2[-1])
leng2= leng2[1::]

visited2 = visited2[::-1]
leng2 = leng2[::-1]


res = 0
for i in range(n):
    if visited2[i] == visited[i]:
        res = max(res, leng[i] + leng2[i] - 1)
    else:
        res = max(res, leng[i] + leng2[i] - 1)

print(res)