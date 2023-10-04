n = int (input())

arr = list(map(int, input().split()))

m = int(input())

arr2 = list(map(int,input().split()))

arr.sort(reverse = True)
arr2.sort(reverse =True)

crain = [0] * n
if arr2[0] > arr[0]:
    print(-1)
    exit()

for i in range(m):
    j = 0
    for k in range(n):
        if arr[k] >= arr2[i] and crain[j] > crain[k]:
            j = k
    crain[j] += 1
            
print(max(crain))
