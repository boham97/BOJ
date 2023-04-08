import sys, math
N = int(input())
arr = [[0]* (N+1) for _ in range(N+1)]
ans = [0] * (N+1)
for i in range(N+1):
    print(f'? {i+1}')
    sys.stdout.flush()
    b = input()
    ans[i]= int(input())
for i in range(N+1):
    for j in range(N+1):
        arr[i][j] = (i+1)**j

for i in range(N+1):
    for j in range(N+1):
        if i == j:
            continue
        else:
            # num = arr[j][i]/arr[i][i]
            num = math.lcm(arr[j][i], arr[i][i])
            j_mul = num//arr[j][i]
            i_mul = num//arr[i][i]
            for k in range(N+1):
                # arr[j][k] -= num*arr[i][k]
                arr[j][k] = j_mul * arr[j][k] - i_mul * arr[i][k]
            # ans[j] -= num*ans[i]
            ans[j] = j_mul * ans [j] - i_mul * ans[i]
            

for i in range(N+1):
    ans[i] = round(ans[i]/arr[i][i])
print('!',*ans, flush=True)
