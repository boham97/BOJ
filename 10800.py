import sys

N = int(input())
arr = [[] for _ in range(2001)]
color = [0] * (N+1)
hap = [0] * 2002
ans = [0] * (N+1)

for i in range(1,N+1):
    c,s = map(int,input().split())
    arr[s].append([c,i])

for i in range(1,2001):
    hap[i] += hap[i-1]
    for j,num in arr[i]:
        hap[i+1] += i
        ans[num] = hap[i] - color[j]
    for j,num in arr[i]:
        color[j] += i
for i in range(1,N+1):
    print(ans[i])