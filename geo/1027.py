n = int(input())
h = list(map(int, input().split()))
ans = [0] * n
for i in range(n):
    for j in range(i+ 1, n):
        for k in range(i+1, j):
            if (h[j] - h[i])/(j - i)*(k - i) + h[i] <= h[k]:
                break
        else:
            ans[i] += 1
            ans[j] += 1
    

print(max(ans))
