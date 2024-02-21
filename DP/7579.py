import sys
input = sys.stdin.readline

n, m = map(int, input().split())
memory = list(map(int, input().split()))
cost = list(map(int, input().split()))

arr  = [[0] * (sum(cost) + 1) for _ in range(n+ 1)]

for i in range(n):
    for j in range(len(arr[0])):
        if arr[i][j] > arr[i+1][j]:
            arr[i+1][j] = arr[i][j]
        if cost[i] + j < len(arr[0]) and arr[i][j] + memory[i] > arr[i+1][j+ cost[i]]:
            arr[i+1][j+ cost[i]] = arr[i][j] + memory[i]


for i in range(len(arr[0])):
    if arr[-1][i] >= m:
        print(i)
        break
