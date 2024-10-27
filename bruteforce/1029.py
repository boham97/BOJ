n = int(input())
arr = list(list(map(int, list(input()))) for _ in range(n))
ans = 0
bitmask = [[10] *n for _ in range(1<<n)]
bitmask[1][0] = 0


for i in range(2**n):
    for j in range(n):
        if bitmask[i][j] == 10: continue
        temp = 0
        for k in range(n):
            if i & 1<<k: temp += 1
        ans = max(temp, ans)
        for k in range(n):
            if i & 1<<k: continue
            if bitmask[i][j] <= arr[j][k]:
                bitmask[i | 1<<k][k] = min(arr[j][k], bitmask[i | 1<<k][k])
                

print(ans)
