arr = [0] * 9

for i in range(9):
    arr[i] = input()

print(max(arr))
print(arr.index(max(arr))+1)