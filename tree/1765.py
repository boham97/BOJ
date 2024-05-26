def find(i):
    while i != papa[i]:
        i = papa[i]
    return papa[i]

def check(i):
    while visit[i] == 0 and i != papa[i]:
        visit[i] = 1
        i = papa[i]


def union(i, j):
    i, j = find(i), find(j)
    if i != j:
        if i > j:
            papa[i] = j
            return j
        else:
            papa[j] = i
            return i
    return i
n = int(input())
m = int(input())

papa = [i for i in range(n + 1)]
enemy = [0] * (n + 1)
visit = [0] * (n + 1)
for _ in range(m):
    a, b, c = input().split()
    b, c = int(b), int(c)
    if a == 'F':
        union(b, c)
    else:
        if enemy[b] == 0:
            enemy[b] = c
        else:
            enemy[b] = union(enemy[b], c)
            
        if enemy[c] == 0:
            enemy[c] = b
        else:
            enemy[c] = union(enemy[c], b)
for i in range(1, n + 1):
    if visit[i]:
        continue
    check(i)
print(visit.count(0) - 1)
