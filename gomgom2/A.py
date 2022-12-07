N = int(input())
ans = 0
for i in range(N):
    temp = input()
    temp = int(temp[2::])
    if temp <= 90:
        ans += 1
print(ans)
