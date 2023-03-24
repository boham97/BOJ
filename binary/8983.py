import sys
input = sys.stdin.readline

M, N, L = map(int, input().split())
hunter = list(map(int, input().split()))
hunter.append(1e10)
hunter.insert(0, -1 * 1e10)
hunter.sort()
ans = 0
for i in range(N):
    n, m = map(int, input().split())
    start = 0
    end = M + 1
    while 1:
        mid = (start + end)//2
        if n > hunter[mid]:
            start = mid + 1
        elif n < hunter[mid]:
            end = mid
        if hunter[mid-1] < n <=hunter[mid]:
            if abs(hunter[mid-1] -n) + m <= L or abs(hunter[mid] -n) + m <= L:
                ans += 1
            break
print(ans)