M, N = map(int, input().split())

stores = int(input())
arr = [0] *(stores)
for i in range(stores):
    x,y, = map(int, input().split())
    if x == 1:
        arr[i] = y
    elif x == 2:
        arr[i] = 2*M+ N - y
    elif x == 3:
        arr[i] = 2*M +2*N -y
    elif x== 4:
        arr[i] = M + y

dong = 0
x,y, = map(int, input().split())
if x == 1:
    dong = y
elif x == 2:
    dong = 2*M + N - y 
elif x == 3:
    dong = 2*M +2*N -y
elif x== 4:
    dong = M + y

ans = 0
for i in range(stores):
    temp1 = max(arr[i], dong)
    temp2 = min(arr[i], dong)
    ans += min(temp1-temp2, 2*M+2*N-temp1+temp2)
print(ans)