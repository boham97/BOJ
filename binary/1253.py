from bisect import bisect_left, bisect_right

N = int(input())

arr =list(map(int, input().split()))

arr.sort()

ans = 0
for i in range(N):
    for j in range(N):
        temp1 = bisect_left(arr,arr[i]-arr[j])
        temp2 = bisect_right(arr,arr[i]-arr[j])
        if temp1<N-1 and arr[temp1]+arr[j]-arr[i] == 0 and not(i==j or i==temp1 or j == temp1):
            ans += 1
            break
        elif arr[temp2-1]+arr[j]-arr[i] == 0 and not(i==j or i==temp2-1 or j == temp2-1):
            ans += 1
            break
print(ans)