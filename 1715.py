import heapq

n = int(input())
hp = []

for _ in range(n):
    heapq.heappush(hp, int(input()))


ans = 0
while len(hp) > 1:
    num1 = heapq.heappop(hp)
    num2 = heapq.heappop(hp)
    ans += (num1 + num2)
    heapq.heappush(hp, num1+num2)


print(ans)
