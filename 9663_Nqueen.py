def f(i, N):
    global ans
    if i == N:
        ans += 1
        #print(ans)
        return
    else:
        for j in range(i, N):
            mat[i], mat[j] = mat[j], mat[i]
            for k in range(i):
                if abs(k-i) == abs(mat[k]- mat[i]):
                    break
            else:
                f(i+1,N)
            mat[i], mat[j] = mat[j], mat[i]

N = int(input())
ans = 0
mat = list(range(N))
for i in range(N//2):
    mat[0], mat[i] = mat[i], mat[0]
    f(1,N)
    mat[0], mat[i] = mat[i], mat[0]
ans = ans *2
if N % 2 == 1:
    mat[0], mat[N//2] = mat[N//2], mat[0]
    f(1,N)
    mat[0], mat[N//2] = mat[N//2], mat[0]
    
print(ans)