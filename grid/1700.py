from heapq import heappush, heappop,heapify
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))
cnt = [[] for _ in range(k+1)]
visit = [1000] * (k+1)
for i in range(k):
    cnt[arr[i]].append(i)
for i in range(k+1):
    if cnt[i]:
        visit[i] = cnt[i][0]
    cnt[i].append(1000)

tab = [0] * n
ans = 0
for i in arr:
    target = 0
    for j in range(n):
        if tab[j] == i:
            for k in cnt[i]:
                if k > visit[i]:
                    visit[i] = k
                    break
            break
            
        else:
            if visit[tab[j]] > visit[tab[target]] or tab[j] == 0:
                target = j
    else:
        if tab[target] != 0:
            ans += 1
        tab[target] = i
        for k in cnt[i]:
            if k > visit[i]:
                visit[i] = k
                break
print(ans)
