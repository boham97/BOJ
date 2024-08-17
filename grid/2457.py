n = int(input())
arr = []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    arr.append((100*a + b, 100*c + d))
arr.append((0, 0))
arr.sort()
end = 301
ans = 0

#print(*arr, sep = '\n')

i = 0
while i <= n and end <= 1130:
    temp = 0
    index = 0
    j = i + 1
    while j <= n and arr[j][0] <= end:
        if temp < arr[j][1]:
            temp =arr[j][1]
            index = j
        j += 1
    #print(arr[i], i, index, end)
    if temp == 0:
        break
    else:
        end = temp
        i = index
        ans += 1
    
        
print(ans if end > 1130 else 0)
