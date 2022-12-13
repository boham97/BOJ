from bisect import bisect_left, bisect_right
N = int(input())

arr = list(map(int, input().split()))
arr.sort()

ans = 1e11
print_arr = []
for num in arr:
    x = bisect_left(arr,-num)
    if abs(arr[x-1]+num) < ans and arr[x-1] != num:
        ans = abs(arr[x-1]+num)
        print_arr = [num, arr[x-1]]
    if x<N and abs(arr[x]+num) < ans  and arr[x] != num:
        ans = abs(arr[x]+num)
        print_arr = [num, arr[x]]

print_arr.sort()
print(*print_arr)

#https://www.acmicpc.net/problem/2470