arr = [[0]*11 for _ in range(4)]
arr[1][1] = 1
arr[2][2] = 1
arr[3][3] = 1

for i in range(1,11):
    for j in range(1,4):
        for k in range(1,4):
            if i+j < 11:
                arr[j][i+j] += arr[k][i]

T = int(input())
for test in range(T):
    num = int(input())
    print(arr[1][num]+arr[2][num]+arr[3][num])