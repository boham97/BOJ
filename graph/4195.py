import sys
input = lambda: sys.stdin.readline().rstrip()

def find(a):
    while arr[a] != a:
        a = arr[a]
    return a

def union(a, b):
    if a == b:
        return cnt[a]
    if rank[a] == rank[b]:
        rank[a] += 1

    if rank[a] > rank[b]:
        arr[b] = a
        cnt[a] += cnt[b]
        return cnt[a]
    else:
        arr[a] = b
        cnt[b] += cnt[a]
        return cnt[b] 


n = int(input())
for _ in range(n):
    m = int(input())
    diction = {}
    cnt = [1] * (2 * m)
    rank = [1] * (2 * m)
    arr = [i for i in range(2 * m)]
    i = 0
    for _ in range(m):
        a, b = input().split()
        if a not in diction:
            diction[a] = i
            i += 1
        if b not in diction:
            diction[b] = i
            i += 1
        print(union(find(diction[a]), find(diction[b])))
    
