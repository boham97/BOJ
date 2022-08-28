N = int(input())
arr = list(map(int,input().split()))
B, C = map(int,input().split())
ans = N
for ban in arr:
    ban -= B
    if ban <= 0:
        continue
    else:
        ans += ban//C
        if ban % C:
            ans += 1
print(ans)