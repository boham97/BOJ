from collections import deque

N, W, L = map(int, input().split())
trucks = list(map(int, input().split()))
trucks.append(L)
time = 0
on = 0
que = deque()

for truck in trucks:
    move = False
    while on + truck > L or len(que)>= W:
        t, created_at = que.popleft()
        on -= t
        time = created_at + W
        move = True
        print("move")
    if not move:
        time += 1
    que.append((truck, time))
    on += truck
    print(time, truck)
