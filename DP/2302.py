def fibo(n):
    if n <=len(Fibo):
        return Fibo[n-1]
    else:
        Fibo.append(fibo(n-2) + fibo(n-1))
        return Fibo[n-1]
Fibo = [1,1]
N = int(input())
M = int(input())
arr = [0]
ans = 1
for i in range(41):
    fibo(i)

for i in range(M):
    arr.append(int(input()))
    ans *= fibo(arr[-1]-arr[-2])
arr.append(N+1)
ans *= fibo(arr[-1]-arr[-2])

print(ans)