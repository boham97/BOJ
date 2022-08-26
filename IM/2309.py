arr = [0]*9
for i in range(9):
    arr[i] = int(input())
arr.sort()
logic = 0
for i in range(8):
    for j in range(i+1,9):
        ans = 0
        for k in range(9):
            if k != i and k != j:
                ans += arr[k]
        if ans == 100:
            arr.remove(arr[j])
            arr.remove(arr[i])
            logic = 1
            break
    if logic == 1:
        break
for i in range(7):
    print(arr[i])
