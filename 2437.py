import sys

input = sys.stdin.readline

N =int(input())
ans = 1

arr = list(map(int, input().split()))
arr.sort()


for i in arr:
    if ans < i:
        break
    ans += i

print(ans)
