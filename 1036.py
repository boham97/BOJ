N = int(input())

arr = [0] * 36

for _ in range(N):
    num = input()
    leng = len(num)

    for i in num:
        if ord(i) >= 65:
            arr[ord(i)-55] += 36 ** (leng - 1)
        else:
            arr[int(i)] += 36 ** (leng - 1)
        leng -= 1
M = int(input())
print(arr)
while M:
    target = 0
    for i in range(35):
        if  (35-i) * arr[i] >=  (35-target) * arr[target]:
            target = i
    
    arr[35] += arr[target]
    arr[target] = 0
    M -= 1
print(arr)



temp = 0

for i in range(36):
    temp += i*arr[i]
ans = ''
while temp > 0:
    if temp%36 >= 10:
        ans += chr(55 + int(temp%36))
    else:
        ans += str(int(temp%36))
    temp //= 36
if ans == '':
    print('0')
else:
    print(ans[::-1])
