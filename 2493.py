import sys
input = sys.stdin.readline

N = int(input())

arr = list(map(int, input().split()))
stack = []
ans = []
for i in range(N):
    if stack == []:
        stack.append(i)
        ans.append(0)
    else:
        while stack:
            if arr[stack[-1]] < arr[i]:
                stack.pop()
            else:
                ans.append(stack[-1] + 1)
                stack.append(i)
                break
        else:
            ans.append(0)
            stack.append(i)

print(*ans)
