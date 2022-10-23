N = int(input())
stair = [0]* (N+1)
ans = [[0]*(N+1) for _ in range(2)]

for i in range(1,N+1):
    stair[i] = int(input())

ans[1][1] = stair[1]
if N > 1:
    ans[1][2] = stair[2]

for i in range(1,N):
    if ans[0][i] and i+2 <= N:
        ans[1][i+2] = max(ans[1][i+2], ans[0][i] + stair[i+2])
    if ans[1][i]:
        if i+2 <= N:
            ans[1][i+2] = max(ans[1][i+2], ans[1][i] + stair[i+2])
        if i+1 <= N:
            ans[0][i+1] = max(ans[0][i+1], ans[1][i] + stair[i+1])

print(max(ans[1][-1], ans[0][-1]))