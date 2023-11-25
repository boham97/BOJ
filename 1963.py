from collections import deque

def find():
    for i in range(2, 10000):
        if (arr[i] == 0):
            for j in range(2, 10000//i + 1):
                arr[i * j] = 1

def solution(x, y):
    que = deque()
    que.append(x)
    visit = [0] * 10000;
    visit[x] = 1
    while que:
        now = que.popleft()
        if now <= 1000:
            continue
        if now == y:
            print(visit[now] - 1)
            break
        else:
            for i in (1, 10, 100, 1000):
                nxt = now - (now%(i * 10)//i * i)
    
                for j in range(0, 10):
                    if visit[nxt + i *j] == 0 and arr[nxt + i * j] == 0:
                        que.append(nxt + i *j)
                        visit[nxt + i * j] = visit[now] + 1

    else:
        print("Impossible")
        
arr = [0] * 10001;
find()
n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    solution(x, y)
    
