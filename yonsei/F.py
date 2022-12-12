import sys
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
            num = arr[j][i]/arr[i][i]
            for k in range(N+1):
                arr[j][k] -= num*arr[i][k]
            ans[j] -= num*ans[i]

print('! ', end='')
for i in range(N+1):
    print(int(ans[i]//arr[i][i]),end = ' ')
sys.stdout.flush()
