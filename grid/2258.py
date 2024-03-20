import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ans = 1e10
arr = list(list(map(int, input().split())) for _ in range(n))
arr.sort(key = lambda x :  (x[1], -x[0]))

j = 0
dum = 0
temp = 0
cost = 0
weight = 0
for i in range(n):
    while arr[j][1] != arr[i][1]:
        dum += arr[j][0]
        j += 1
        weight = dum
        cost = 0
    cost += arr[i][1]
    weight += arr[i][0]
    if weight >= m and cost < ans:
        ans = cost

print(ans if ans != 1e10 else -1)

    
