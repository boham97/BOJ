arr1 = list(input())
arr2 = list(input())
ans = [0] * len(arr1)
N = len(arr1)
for x in arr2:
    point = N+1
    if x in arr1:
        point = arr1.index(x)
        ans[point] += 1
    for i in range(point,N):
        ans[i] = max(ans[i-1],ans[i])
    if point != N+1:
        arr1[point] = '0'

    print(ans)
