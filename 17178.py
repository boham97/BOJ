t = int(input())
stack = []
arr = []
turn = 0

for _ in  range(t):
    temp = list(input().split())
    for i in range(5):
        a = temp[i]
        if len(temp[i]) == 3:
            a = a[:2] + "00" + a[2:]
        elif len(temp[i]) == 4:
            a = a[:2] + "0" + a[2:]
        arr.append(a)
        
        
ans = sorted(arr)

for txt in arr:
    stack.append(txt)
    while stack and stack[-1] == ans[turn]:
        stack.pop()
        turn += 1
print("BAD" if len(stack) else "GOOD")
