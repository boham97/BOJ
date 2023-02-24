import sys
N, M = map(int, sys.stdin.readline().split())

arr = list(map(int, sys.stdin.readline().split()))
arr2 = [0 for _ in range(N +1)]

for i in range(1,N+1):
    arr2[i] = arr2[i-1] + arr[i-1]

for k in  range(M):
    i, j = map(int, sys.stdin.readline().split())
    print(arr2[j] - arr2[i-1])
