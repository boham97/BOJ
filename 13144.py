import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
ans = 0
mat = [True] * 100001

start, end = 0, 0
while start < n and end < n:
    if mat[arr[end]]:
        mat[arr[end]] = False
        end += 1
        ans += end - start
    else:
        mat[arr[start]] = True
        start += 1
print(ans)           
