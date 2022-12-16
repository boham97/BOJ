N, C = map(int, input().split())

arr = [0]* N
for i in range(N):
    arr[i] = int(input())
arr.sort()

start = 0
end = arr[N-1]
ans = 0

while start <= end:
    mid = (start + end)//2
    cnt = 1
    temp = 0
    for i in range(N):
        print(arr[i]-arr[temp] >= mid, arr[i], arr[temp])
        if arr[i]-arr[temp] >= mid:
            temp = i
            cnt += 1
    if cnt >= C:
        start = mid + 1
        if mid>ans:
            ans = mid

    elif cnt < C:
        end = mid - 1

print(ans)