def dfs(day, pay):
    global N, max_pay
    if day > N:
        return
    elif day == N:
        if pay > max_pay:
            max_pay = pay
    else:
        dfs(day+arr[day][0],pay+arr[day][1])
        dfs(day+1,pay)

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
max_pay = 0
dfs(0,0)
print(max_pay)