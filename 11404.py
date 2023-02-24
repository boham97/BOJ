""" 플로이드 그리드"""

import sys

inf = 100 * 1000000
input = sys.stdin.readline

N = int(input())
M = int(input())

arr = [[inf] * (N+1) for _ in range(N + 1)]
for i in range(1 + N):
    arr[i][i] = 0
"""잛은 간선으로 갱신"""
for _ in range(M):
    a, b, c = map(int, input().split())
    arr[a][b] = min(arr[a][b], c)

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if arr[i][j]:
            for k in range(1, N + 1):
                arr[j][k] = min(arr[j][k], arr[j][i] + arr[i][k])

for i in range(1, N + 1):
    for j in range(1, N + 1):
        print(arr[i][j] if arr[i][j] < inf else 0, end = ' ')
    print()
