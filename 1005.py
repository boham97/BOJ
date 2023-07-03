from collections import deque

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    time = list(map(int, input().split()))
    index = [0] * (N + 1)
    srt = [0] * (N +1)
    arr= [[] for _ in range(N+1)]
    que = deque()
    for _ in range(K):
        a, b = map(int, input().split())
        arr[a].append(b)
        index[b] += 1
    for i in range(1,N+1):
        if index[i] == 0:
            que.append(i)
            srt[i] = time[i-1]
    ans = []
    while que:
        now = que.popleft()
        ans.append(now)
        for i in arr[now]:
            index[i] -= 1
            srt[i] = max(srt[i], srt[now] + time[i-1])
            if index[i] == 0:
                que.append(i)

    target = int(input())
    print(srt[target])


