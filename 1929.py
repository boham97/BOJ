N, M = map(int, input().split())
visited = [1] * (M+1)
visited[0], visited[1] = 0, 0
i = 2
while i <= M**0.5:
    if visited[i]:
        j = 2
        while i*j<=M:
            visited[i*j] = 0
            j += 1
    i += 1

for i in range(N, M+1):
    if visited[i]:
        print(i)
