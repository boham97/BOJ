x = int(input())
y = int(input())
ans = 0
if x >0:
    if y>0:
        ans = 1
    else:
        ans = 4
else:
    if y>0:
        ans = 2
    else:
        ans = 3

print(ans)
