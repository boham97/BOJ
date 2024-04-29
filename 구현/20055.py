n, k = map(int, input().split())

arr = list(map(int ,input().split()))
robot = [0] * (2*n)

end = n - 1
ans = 0
while  k>0:
    #1
    now = 0
    robot[end] = 0
    end = end - 1 if end > 0 else end -1 + 2* n
    robot[end] = 0
    #2
    for i in range(n):
        now = end - i if end - i >= 0 else end - i + 2 * n
        if arr[now]and robot[now] == 0 and robot[now -1]:
            arr[now] -= 1
            if arr[now] == 0:
                k -= 1
            robot[now] = 1
            robot[now - 1] = 0
    #3
    if arr[now] != 0:
        robot[now] += 1
        arr[now] -= 1
        if arr[now] == 0:
            k -= 1

    ans += 1

    
print(ans)
