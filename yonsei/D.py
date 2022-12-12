N = int(input())
temp = input()
stack = []
ans = 0

for i in range(N):
    if len(stack) == 0 or stack[-1] == temp[i]:
        stack.append(temp[i])
        if ans < len(stack):
            ans = len(stack)
    elif stack[-1] != temp[i]:
        stack.pop()
    
if stack:
    print(-1)
else:
    print(ans)