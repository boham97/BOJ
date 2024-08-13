n, m = map(int, input().split())
node = [[] for _ in range(n + 1)]
cnt = [0] * (n + 1)

ans = []
for _ in range(m):
    arr = list(map(int, input().split()))
    for i in range(2, arr[0]  + 1):
        node[arr[i - 1]].append(arr[i])
        cnt[arr[i]] += 1
print(node)
print(cnt)

stack = []
for i in range(1, n + 1):
    if cnt[i] == 0:
        stack.append(i)

while stack:
    now = stack.pop()
    ans.append(now)
    for i in node[now]:
        cnt[i] -= 1
        if cnt[i] == 0:
            stack.append(i)


if len(ans) == n:
    print(*ans, sep='\n')
else:
    print(0)
