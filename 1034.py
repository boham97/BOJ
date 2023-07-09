N, M = map(int, input().split())
arr = list(list(map(int, list(input()))) for _ in range(N))
K = int(input())
streak = 0

def dfs(k, m, now):
    global streak
    if m == M or sum(now) <= streak:
        if sum(now) > streak and k%2 == K%2:
            streak = sum(now)
    else:
        if k < K:
            temp = [0] * N
            for i in range(N):
                if now[i] and arr[i][m] == 0:
                    temp[i] = 1
                else:
                    temp[i] = 0
            dfs(k+1, m+1, temp)    
        temp = [0] * N
        for i in range(N):
            if now[i] and arr[i][m]:
                temp[i] = 1
            else:
                temp[i] = 0
        dfs(k, m+1, temp)
        
srt = [0] * N
for i in range(N):
    if arr[i][0]:
        srt[i] = 1

dfs(0, 1, srt)

for i in range(N):
    if arr[i][0] == 0:
        srt[i] = 1
    else:
        srt[i] = 0
dfs(1, 1, srt)


print(streak)
