n, k = map(int, input().split())
arr = input()
stack = []

for c in arr:
    while k and stack and stack[-1] <int(c):
        stack.pop()
        k -= 1
    stack.append(int(c))

while k:
    stack.pop()
    k -= 1

for s in stack:
    print(s, end='')
