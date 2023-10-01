n, k = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))

bit = [[10000]* (n) for _ in range(1<<n)]
bit[1<<k][k] = 0
i = 1 << k
while i < 1 <<n:
    for j in range(n):
        for h in range(n):
            temp = bit[i][j] + arr[j][h]
            if j == h:
                continue
            if (i >> h) %2 == 1:
                if bit[i][h] > temp:
                    bit[i][h] = temp
                    i -= 1
                
            else:
                if i + (1<<h) < 1<< n and bit[i + (1<<h)][h] > temp:
                    bit[i + (1<<h)][h]  = temp
    i += 1
                    

print(min(bit[-1]))

