from collections import deque
import sys
N = int(input())
for i in range(N):
    x,y = map(int,sys.stdin.readline().split())
    temp = list(map(int,sys.stdin.readline().split()))
    temp = temp[1::]

    ans1 = [0]*(200001)
    ans1[100000] = 1
    que = deque()
    que.append(0)
    flag = 0

    while que:
        point = que.popleft()
        for i in temp:
            if -100000<=point+i<=100000 and not ans1[point+100000+i]:
                que.append(point+i)
                ans1[point+100000+i] = 1
            if -100000<=point-i<=100000 and not ans1[point+100000-i]:
                que.append(point-i)
                ans1[point+100000-i] = 1
    if ans1[x+100000]:
        ans1 = [0]*(200001)
        ans1[100000] = 1
        que = deque()
        que.append(0)
        while que:
            if ans1[y+100000] == 1:
                flag = 1
                break
            point = que.popleft()
            for i in temp:
                if -100000<=point+i<=100000 and not ans1[point+100000+i]:
                    que.append(point+i)
                    ans1[point+100000+i] = 1
                if -100000<=point-i<=100000 and not ans1[point+100000-i]:
                    que.append(point-i)
                    ans1[point+100000-i] = 1
    if flag == 0:
        print('Gave up')
    else:
        print('Ta-da')