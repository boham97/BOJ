import sys
input = sys.stdin.readline

n = int(input())

arr = list(list(map(int, input().split())) for _ in range(n))

arr.sort(key = lambda x: x[1], reverse = True)

time = arr[0][1]

for cost, end in arr:
    if time > end:
        time = end
    time -= cost

print(time if time >= 0 else -1)
