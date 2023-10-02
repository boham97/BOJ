a, b = map(str, input().split())
ans = 100
for i in range(len(b)- len(a)+1):
    temp = 0
    for j in range(len(a)):
        if a[j] != b[i+j]:
            temp += 1
    if temp < ans:
        ans = temp
print(ans)
