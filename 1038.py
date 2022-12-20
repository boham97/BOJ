# 감소하는수
# https://www.acmicpc.net/problem/1038 
# 브루트포스

N = int(input())
ans = -1
i = 0
while i<=9876543210:
    num =i
    temp = -1
    stage = 0
    while num:
        if num%10 > temp:
            temp = num % 10
            num //= 10
            stage += 1
        else:
            stage -= 1
            i += 10**(stage)
            break
    else:
        ans += 1
        if ans == N:
            print(i)
            break
        stagge = 0
        i += 1
else:
    print(-1)
