import sys
input = lambda: sys.stdin.readline().rstrip()

def find(a):
    while arr[a] != a:
        a = arr[a]
    return a

def union(b, c):
    if b != c:
        b, c = max(b,c), min(b,c)
        arr[c] =b


n, m = map(int, input().split())
arr = [i for i in range(n +1)]
for _ in range(m):
    a, b,c = map(int,input().split())
    if a:
        print( "YES" if find(b) == find(c) else "NO")
    else:
        union(find(b), find(c))
