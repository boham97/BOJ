n= int(input())
arr = sorted(list(map(int, input().split())))
ans = 1e10
fluid = [0, 0, 0]
for i in range(n-1):
    left, right = i + 1, n - 1

    while left < right:
        res = arr[i] + arr[left] + arr[right]
        if abs(res) < ans:
            ans = abs(res)
            fluid = [arr[i], arr[left], arr[right]]

        if res < 0:
            left += 1
        elif res > 0:
            right -= 1
        else:
            print(*fluid)
            exit()
            
print(*fluid)
