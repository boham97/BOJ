import sys
input = lambda : sys.stdin.readline().rstrip()

n, m = map(int, input().split())
arr = list(map(int, input().split()))
cnt = [0] * 1000
ans = 0
last = 0
cnt[0] = 1
for i in arr:
    last = (last +i)%m
    cnt[last] += 1

for i in cnt:
    ans += i * (i - 1)//2

print(ans)
