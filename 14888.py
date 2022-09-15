def choose(n, temp):
    global ans1, ans2
    if n == N-1:
        if temp > ans2:
            ans2 = temp
        if temp < ans1:
            ans1 = temp
        return
    for i in range(4):
        if cal[i] == num[i]:
            continue
        else:
            num[i] += 1
            if i == 0:
                choose(n+1, temp + arr[n+1])
            elif i == 1:
                choose(n+1, temp - arr[n+1])
            elif i == 2:
                choose(n+1, temp * arr[n+1])
            elif i == 3:
                if temp > 0:
                    choose(n+1, temp // arr[n+1])
                else:
                    choose(n+1, -1*(-1*temp//arr[n+1]))
            num[i] -= 1

N = int(input())
arr = list(map(int, input().split()))
cal = list(map(int, input().split()))
ans1 = 10** 10
ans2 = -1* 10 **10
num = [0,0,0,0]
choose(0,arr[0])
print(ans2)
print(ans1)