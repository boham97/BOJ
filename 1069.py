x, y, d, t = map(int, input().split())
t = min(d, t)
distance = (x**2 + y**2)**0.5
jump = distance//d
ans = jump * t
distance -= jump * d
ans += min(distance, - distance + d + t, 2*t)
if jump:
    ans = min(ans, (jump + 1) *t)
print(ans)

