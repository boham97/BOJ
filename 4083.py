import sys
sys.setrecursionlimit(1000)
input = sys.stdin.readline

def find(x):
    if arr[x] != 0:
        return find(arr[x])
    else:
        return x

def union(x, y):
    if find(x) == find(y) :
        return 1
    arr[find(x)] = y
    return 0


case = 1
while case:
    N, M = map(int, input().split())
    if N ==0 and M == 0:
        break
    
    arr = [0] * (N+1)
    ans = 0
    temp = set()
    
    for _ in range(M):
        x, y = map(int, input().split())
        if union(x, y):
            temp.add(x)
            temp.add(y)
    cycle = set()
    for i in temp:
        cycle.add(find(i))
        
    for i in range(1, N+1):
        if arr[i] == 0 and i not in cycle:
            ans += 1


    if ans > 1:
        print(f'Case {case}: A forest of {ans} trees.')
    elif ans == 1:
        print(f'Case {case}: There is one tree.')
    else:
        print(f'Case {case}: No trees.')
    case += 1
