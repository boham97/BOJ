N, K, P, X = map(int, input().split())

def compare(i):
    if y_bit[i] == 10:
        y_bit[i] = 0
        y_bit[i +1] += 1
        compare(i+1)

arr = [[0,1,2,4,5,6],[2,5],[0,2,3,4,6],[0,2,3,5,6,],[1,3,2,5],[0,1,3,5,6],[0,1,4,3,5,6], [0,2,5],[0,1,2,3,4,5,6], [0,1,2,3,5,6]]
bit = [[0] * 7 for _ in range(10)]
dif = [[0] * 10 for _ in range(10)]
ans = 0

for i in range(10):
    for j in arr[i]:
        bit[i][j] = 1

for i in range(10):
    for j in range(10):
        for k in range(7):
            dif[i][j] += 1 if bit[i][k] + bit[j][k] == 1 else 0

x_bit = [0] * k
for i in range(k):
    x_bit[i] = X% 10
    X = X// 10

y_bit = [0] * (k + 1)
for i in range(1, N+ 1):
    y_bit[0] += 1
    compare(0)
    temp = 0
    for j in range(K):
        temp += dif[x_bit[j]][y_bit[j]]
    if temp <= P:
        ans += 1

print(ans - 1)

