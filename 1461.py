n,m = map(int, input().split())

arr = list(map(int, input().split()))

minus = []
plus = []

ans = 0
for i in arr:
    if i < 0:
        minus.append(-i)
    else:
        plus.append(i)

minus.sort(reverse = True)
plus.sort(reverse = True)

for i in range(0,len(minus),m):
    ans += minus[i] * 2
for i in range(0, len(plus), m):
    ans += plus[i] * 2
    
left, right = 0, 0
if minus:
    left = minus[0]
if plus:
    right = plus[0]

ans -= max(left, right)

print(ans)
