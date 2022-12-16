N, C = map(int, input().split())

arr = [0]* N
for i in range(N):
    arr[i] = int(input())
arr.sort()

start = 0
end = arr[-1] * C
ans = arr[-1] * C

while start <= end:
    mid = (start + end)//2
    cnt = 0
    for i in range(N):
        cnt += mid//arr[i]
    if cnt >= C:
        end = mid - 1
        if mid<ans:
            ans = mid
    elif cnt < C:
        start = mid + 1

print(ans)