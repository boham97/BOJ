from heapq import heappush, heappop

heap = []
now = []
ans = 1
N = int(input())

for _ in range(N):
    x, y = map(int, input().split())
    heappush(heap, (x,y))

for _ in range(N):
    x, y = heappop(heap)
    if now == []:
        heappush(now, y)
    elif x >= now[0]:
        heappop(now)
        heappush(now, y)
        
    else:
        heappush(now, y)
        if len(now) > ans:
            ans += 1
        

print(ans)


//우선순위 큐를 쓰면 강의실 배정을 탐욕적이지 않게 풀수 있어요!
