num = int(input())
arr = []
while num:
    arr.append(num%10)
    num = num//10

hap1 = 0
hap2 = 0
for i in range(len(arr)//2):
    hap1 += arr[i]
    hap2 += arr[-1*i-1]

if hap1 == hap2:
    print('LUCKY')
else:
    print('READY')
