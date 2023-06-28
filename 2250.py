def func(node):
    if node == 0:
        return
    func(arr[1][node])

    if visit[node]:
        visit[node] = 0
        now = node
        arr[4][now] -= 1
        for i in range(N+1):
            if arr[4][i] > arr[4][now]:
                arr[4][i] += 1
        arr[4][now] += 1
    func(arr[2][node])

def func2(node, h):
    if node == 0:
        return
    arr[3][node] = h
    func2(arr[1][node], h+1)
    func2(arr[2][node], h+1)

N = int(input())
arr = [[0] * (N+1) for _ in range(6)]

for _ in range(N):
    a, b, c = map(int, input().split())
    if b != -1:
        arr[1][a] = b
        arr[5][b] = a
    if c != -1:
        arr[2][a] = c
        arr[5][c] = a
root = 0
visit = [0] * (N+1)
for i in range(N+1):
    visit[arr[1][i]] = 1
    visit[arr[2][i]] = 1

for i in range(N+1):
    if visit[i] == 0:
        root = i
        visit[i] = 1
        break

arr[4][0] = -1
func(root)
func2(root, 1)


ans = -1
h = 0
for k in range(1, max(arr[3])+1):
    temp = []
    for i in range(N+1):
        if arr[3][i] == k:
            temp.append(arr[4][i])
    now = max(temp) - min(temp)
    if ans < now:
        ans = now
        h = k

print(h,ans +1)


