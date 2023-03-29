import heapq
import sys

input = sys.stdin.readline

N = int(input())


que = list(map(int, input().split()))
heapq.heapify(que)
for i in range(1,N):
    arr = list(map(int, input().split()))
    for j in range(N):
        heapq.heappushpop(que, arr[j])


print(heapq.heappop(que))