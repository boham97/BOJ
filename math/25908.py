s, t = map(int, input().split())
ans = 0
for i in range(1, t+ 1):
    for j in range(s//i + (1 if s%i else 0), t//i + 1):
        ans += -1 if i%2 else 1

print(ans)
