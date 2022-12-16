def fac(n):
    if n == 1 or n==0:
        return 1
    else:
        return n*fac(n-1)

T = int(input())
for _ in range(T):
    N, M = map(int,input().split())
    if M > N:
        N, M = M, N
    ans = fac(N)//(fac(M)*fac(N-M))
    print(ans)