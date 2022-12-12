from sys import stdin
from collections import deque

N, M = map(int,input().split())
arr = list(map(int, stdin.readline().split()))
que = deque()

i = 0
length = 0
num  = 1*1e10
life = 1
while i<N:
    while que and que[-1][1] > arr[i]:  #새로 들어온 수보다 크면 pop
        que.pop()
    while que and que[0][0] <= i-M:    #범위 벗어나는 거 pop
        que.popleft()
    que.append([i,arr[i]])              #index와 수 저장
    i += 1
    print(que[0][1], end= ' ')