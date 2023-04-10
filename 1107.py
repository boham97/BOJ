def dfs(guess, depth):
    global N, ans
    if ans > min(abs(N-guess)+len(str(guess)), abs(N-100)):
        ans = min(abs(N-guess)+len(str(guess)), abs(N-100))
    if depth > len(str(N)):
        return
    for i in range(10):
        if i not in arr:
            dfs(guess*10 +i, depth+1)

ans = 1e7

N = int(input())
M = int(input())

arr = []
if M != 0:
    arr = list(map(int, input().split()))

for i in range(10):
    if i not in arr:
        dfs(i,1)
if M == 10:
    print(abs(N-100))
else:
    print(ans)
