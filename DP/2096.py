N = int(input())
dp1 = [0,0,0]
dp2 = [0,0,0]
for i in range(N):
    arr = list(map(int, input().split()))
    temp1 = [-1] * 3
    temp2 = [1000000] * 3
    for j in range(3):
        for k in range(-1,2):
            if 0 <= j+k < 3:
                if temp1[j+k] < dp1[j]+arr[j+k]:
                    temp1[j+k] = dp1[j]+arr[j+k]
                if temp2[j+k] > dp2[j]+arr[j+k]:
                    temp2[j+k] = dp2[j]+arr[j+k]
    dp1 = temp1[:]
    dp2 = temp2[:]
print(max(dp1), min(dp2))

