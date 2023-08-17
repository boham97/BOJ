from sys import stdin
input = stdin.readline

N = int(input())
arr = []

for _ in range(N):
    a, b = map(int, input().split())
    arr.append((a, 1))
    arr.append((b, -1))

arr.sort()
ans , cnt = 0, 0

for i in range(2*N):
    cnt += arr[i][1]
    if cnt > ans:
        ans = cnt

print(ans)
