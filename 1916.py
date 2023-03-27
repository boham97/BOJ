N = int(input())
M = int(input())

arr = list([1e9] * (N + 1) for _ in range(N +1))

for _ in range(M):
    n, m , c = map(int, input().split())
    arr[n][m] = min(arr[n][m], c)

for i in range(N+1):
    arr[i][i] = 0

srt, end = map(int, input().split())

visited = [0] * (N+1)
distance = [1e9] * (N+1)

for i in range(N+1):
    distance[i] = arr[srt][i]

visited[srt] = 1

for i in range(1, N+1):
    min_d = 1e9
    next = 0
    for j in range(1, N+1):
        if not visited[j] and distance[j] < min_d:
            next = j
            min_d = arr[i][j]
    visited[next] = 1
    for j in range(1, N+1):
        if not visited[j]:
            distance[j] = min(distance[j], distance[next] + arr[next][j])

print(distance[end])

#  출방지점에서 방문하지 않은 곳 중에 가장 가까운곳 ㄲㄲ
# 해당 지점을 경유하는 거리와 현재 경로 비교
# 방문 처리