N, S = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()
ans = 0

for i in range(2**N):
    temp = []
    for j in range(N):
        if 1 << j & i:
            temp.append(arr[j]) 
    if sum(temp) == S and temp != []:
        ans += 1
print(ans)
