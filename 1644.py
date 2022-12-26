N = int(input())

arr = [1] * (N+1)
num = [0]
temp = 0
for i in range(2,N+1):
    if arr[i]:
        j = 2
        while j*i <= N:
            arr[i*j] = 0
            j += 1
        num.append(temp+i)
        temp += i

start = 0
end = 0
ans = 0

while end < len(num):
    if num[end] - num[start] > N:
        start += 1
    elif num[end] - num[start] < N:
        end += 1
    else:
        ans += 1
        end += 1

print(ans)