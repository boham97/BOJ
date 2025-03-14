
x, y = map(int ,input().split())
t = y -x
ans = 0
i = 1
while t > 0:
    if t <= i:
        ans += 1
        break
    t -= 2*i
    ans += 2
    i += 1
print(ans)
