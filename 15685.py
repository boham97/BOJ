dd = [[0, 1], [-1, 0], [0, -1], [1, 0]]
N = int(input())
gen = [[] for _ in range(N)]
curves = [[] for _ in range(N)]

for i in range(N):
    buffer = list(map(int, input().split()))
    gen[i] = buffer[3]
    curves[i].append((buffer[1], buffer[0]))
    curves[i].append((buffer[1]+dd[buffer[2]][0], buffer[0]+dd[buffer[2]][1]))
    
for i in range(N):
    for j in range(1,gen[i]+1):
        for k in range(2**(j-1)-1, -1, -1):
            temp1, temp2 = curves[i][k][0]-curves[i][2**(j-1)][0], curves[i][k][1]- curves[i][2**(j-1)][1]
            curves[i].append((curves[i][2**(j-1)][0]+temp2, curves[i][2**(j-1)][1]-temp1))

arr = [[0] * 101 for _ in range(101)]
for i in range(N):
    for x, y in curves[i]:
        if 0 <= x < 101 and 0 <= y < 101:
            arr[x][y] = 1

ans = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] + arr[i][j+1] + arr[i+1][j] + arr[i+1][j+1] == 4:
            ans += 1
print(ans)