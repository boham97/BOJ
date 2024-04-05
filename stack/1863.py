import sys
input = sys.stdin.readline

n = int(input())
stack = [0]
ans = 0
for _ in range(n):
    x, y = map(int, input().split())
    if len(stack) == 0 or stack[-1] < y:
        stack.append(y)
    else:
        while stack and stack[-1] > y:
            stack.pop()
            ans += 1
        if stack and stack[-1] < y:
            stack.append(y)
print(ans + len(stack) - 1)
