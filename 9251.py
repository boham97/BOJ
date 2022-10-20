arr1 = input()
arr2 = input()
arlpha = [0] * 26
ans = [[0] * (len(arr1)+1) for _ in range((len(arr2)+1))]

for i in range(len(arr2)):
    temp = 0
    for j in range(len(arr1)):
        if arr2[i] == arr1[j]:
            ans[i+1][j+1] = ans[i][j] +1
        else:
            ans[i+1][j+1] = max(ans[i+1][j], ans[i][j+1])
print(ans[-1][-1])
