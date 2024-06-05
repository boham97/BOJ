str1 = input().rstrip()
str2 = input().rstrip()

n, m = len(str1), len(str2)

arr = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(n):
    for j in range(m):
        arr[i + 1][j + 1] = (arr[i][j] + 1) if str1[i] == str2[j] else max(arr[i][j + 1], arr[i + 1][j])

ans = ''
i, j = n, m
now = arr[i][j]
while now != 0:
    if arr[i][j - 1] == now - 1 and now - 1 == arr[i - 1][j]:  
        ans = str2[j - 1] + ans  
        now -= 1  
        i -= 1  
        j -= 1  
    else:  
        if arr[i - 1][j] > arr[i][j - 1]:  
            i -= 1  
        else:  
            j -= 1  
print(arr[n][m])
print(ans)

