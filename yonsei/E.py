N = int(input())
ans = 0
arr = [1] *(N+1)
for i in range(2, N+1):
    if arr[i] == 1:
        ans += i
        j =2 
        while j* i <= N:
            if arr[j*i] == 1:
                arr[j*i] = 0
                ans += i
            j += 1

print(ans)