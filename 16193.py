N = int(input())
arr = list(map(int, input().split()))

arr.sort()

ans = 0

for i in range(N):
    if i != (N-1)//2:
        ans += abs(arr[i] - arr[N-i-1])

if N%2:
    ans -= min(arr[(N-1)//2] - arr[(N-1)//2- 1], arr[(N-1)//2 + 1] - arr[(N-1)//2])

print(ans)
