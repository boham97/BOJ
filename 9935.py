import sys

input = sys.stdin.readline

arr = list(input())[:-1]
temp = list(input())[:-1]
collect = len(temp)

bomb = {}

for i in range(collect):
    bomb[temp[i]] = i

ans = []

for i in range(len(arr)):

    ans.append(arr[i])
    if arr[i] == temp[-1] and i + 1 >= collect:
        for j in range(collect):
            if ans[(-1-j)] != temp[(-1-j)]:
                break
        else:
            for _ in range(collect):
                ans.pop()


print(''.join(ans)) if len(ans) > 0 else print("FRULA")