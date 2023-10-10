n = int(input())
arr = list(input() for _ in range(n))
nonZero = [0] * 27
mul = [0] * 27
ans = [-1] * 10
visit = [0] * 27

for i in range(n):
    nonZero[ord(arr[i][0])-64] = 1
    size = len(arr[i])
    for j in range(size):
        now = arr[i][size - j - 1]
        mul[ord(now) - 64] += 10 ** j
        visit[ord(now) - 64] = 1
for i in range(9,-1, -1):
    temp = 0
    num = 0
    for j in range(1, 27):
        if visit[j] and temp < mul[j]:
            temp = mul[j]
            num = j
    ans[i] = num
    visit[num] = 0

res = 0

k = 0
while nonZero[ans[k]]:
    ans[k], ans[0] = ans[0], ans[k]
    k += 1
ans[k], ans[0] = ans[0], ans[k]
  


for i in range(10):
    res += mul[ans[i]] * i

print(res)
    
