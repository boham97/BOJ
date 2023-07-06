from bisect import bisect_left, bisect_right

T = int(input())
N = int(input())
arr1 = list(map(int, input().split()))
M = int(input())
arr2 = list(map(int, input().split()))

sum1 = []
sum2 = []

for i in range(N+1):
    for j in range(i):
        sum1.append(sum(arr1[j:i]))

sum1.sort()

for i in range(M+1):
    for j in range(i):
        sum2.append(sum(arr2[j:i]))

sum2.sort()

ans = 0

for i in sum1:
    temp1 = bisect_left(sum2, T - i)
    temp2 = bisect_right(sum2, T - i)
    ans += (temp2 -temp1)


print(ans)
