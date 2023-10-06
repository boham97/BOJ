n = int(input())
arr = list(input() for _ in range(n))
nonZero = [0] * 26
mul = [0] * 26

for i in range(n):
    nonZero[ord(arr[i][0])-65] = 1
    size = len(arr[i])
    for j in range(size):
        now = arr[i][size - j - 1]
        mul[ord(now) - 65] += 10 ** j


for i in range(9, -1, -1):
    temp = 0
    index = 0
    for j in range(26):
        if mul[j] > temp and not visit[j]:
            temp = mul[j]
            index = j
    if temp > 0:
        pass

    
