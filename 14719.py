H, W = map(int, input().split())

arr = list(map(int, input().split()))
visit = [[0] * W for _ in range(H)]


for w in range(W):
    for h in range(H):
        if arr[w] > h:
            visit[h][w] = 1
    
ans = 0

for h in range(H):
    logic = False
    srt  = 0
    for w in range(W):
        if visit[h][w] == 1:
            if logic == True:
                ans += w - srt - 1
                srt = w
            if logic == False:
                logic = True
                srt = w

print(ans)
