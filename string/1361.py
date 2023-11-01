import sys
input = sys.stdin.readline

arr = input()

di = dict()
i = 1
for c in arr:
    di[c] = i
    i += 1
n = len(arr) - 1

ans = 0

password = input()
for c in password:
    if c == '\n':
        continue
    ans = (ans*n +di[c])%900528

print(ans)
    
