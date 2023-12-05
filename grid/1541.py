s = input()
ans = 0
num = ""
logic = False

for i in s:
    if i != '-' and i != '+':
        num += i
    else:
        if logic:
            ans -= int(num)
        else:
            ans += int(num)
        num = ""
    if i == '-':
        logic = True

if logic:
    ans -= int(num)
else:
    ans += int(num)

print(ans)
