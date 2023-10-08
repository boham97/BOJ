n = int(input())
arr = list(map(int, input().split()))

min1 = min(arr)
min2 = 1e7
for i in range(6):
    for j in range(6):
        if i != j and i + j != 5 and arr[i] + arr[j]< min2:
            min2 = arr[i] + arr[j]


min3 = 1e7
for i in range(6):
    for j in range(6):
        if i == j or i + j == 5:
            continue
        for k in range(6):
            if  k == i or k ==j or i + k == 5 or j + k == 5:
                continue
            sum3 = arr[i] + arr[j] + arr[k]
            if sum3 < min3:
                min3 = sum3
                print(i,j,k)

if n == 1:
    print(sum(arr) - max(arr))
else:
    ans = min1 * 5 * (n-2)**2 + min1 * 4 * (n- 2)
    ans += min2 * (n-2) * 8 + min2 * 4
    ans += min3 * 4
    print(ans)
