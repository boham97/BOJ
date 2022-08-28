N = int(input())
arr = [0] * N
highest = 0
for i in range(N):
    arr[i] = list(map(int,input().split()))
    if arr[i][1] > highest:
        highest = arr[i][1]
arr.sort()
ans = 0
temp = 0
for i in range(N):
    if temp > i:
        continue
    for j in range(i+1, N):
        if arr[i][1] <= arr[j][1]:
            ans += arr[i][1] * (arr[j][0]-arr[i][0])
            temp = j
            break
    else:
        high2 = 0
        for k in range(i+1, N):
            if arr[k][1] > high2:
                high2 = arr[k][1]
                temp = k
        ans += arr[i][1]
        ttt= (arr[temp][0] - arr[i][0])
        ans += high2 * (arr[temp][0] - arr[i][0]-1)
print(ans)