T, W = map(int, input().split())
data = []
for _ in range(T):
    data.append(int(input())-1)

data.insert(0,0)
arr = [[0]*(T+1) for _ in range(W+1)]


for j in range(1,T+1):
    if data[j] == 0:
        temp1 = arr[0][j-1] +1
    else:
        temp1 = arr[0][j-1]
    arr[0][j] = temp1

for i in range(1,W+1):
    for j in range(1,T+1):
        if j>=i:
            if data[j] == i%2:
                temp1 = arr[i][j-1] +1
                if 0 < i <= W:
                    temp2 = arr[i-1][j-1]
            else:
                temp1 = arr[i][j-1]
                if 0 < i <= W:
                    temp2 = arr[i-1][j-1] + 1
            arr[i][j] = max(temp1, temp2)


ans = 0
for i in range(W+1):
    if ans < arr[i][-1]:
        ans = arr[i][-1]
print(ans)