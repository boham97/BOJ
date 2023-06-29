import sys

N = int(input())
arr = list(map(int, sys.stdin.readline().split()))

stack = []
ans = []

for i in range(len(arr)-1,-1,-1):
    while stack:
        if stack[-1] > arr[i]:
            ans.append(stack[-1])
            stack.append(arr[i])
            break
        else:
            stack.pop()
    if len(stack) == 0:
        ans.append(-1)
        stack.append(arr[i])

print(*ans[::-1])
