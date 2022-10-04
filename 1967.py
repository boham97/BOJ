N = int(input())
arr = [list(map(int,input().split())) for _ in range(N-1)]
tree = [0] * (N+1)
dist = [0] * (N+1)
parents = set()
for i in range(N-1):
    tree[arr[i][1]] = arr[i][0]
    dist[arr[i][1]] = arr[i][2]
    parents.add(arr[i][0])
if N >1:
    parents.remove(1)
ans = 0
for i in range(1,N+1):
    if i in parents:
        continue
    temp1 = set()
    jasic1 = i
    while jasic1 != 0:
        temp1.add(tree[jasic1])
        jasic1 = tree[jasic1]
    for j in range(1,N+1):
        if j in parents or i == j:
            continue
        gongtong = j
        while gongtong not in temp1:
            gongtong = tree[gongtong]
        temp = 0
        now = i
        while now != gongtong:
            temp += dist[now]
            now = tree[now]
        now = j
        while now != gongtong:
            temp += dist[now]
            now = tree[now]
        if temp > ans:
            ans = temp
        
print(ans)