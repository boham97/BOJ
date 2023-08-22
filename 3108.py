import sys
def find(x):
    return x if x == parent[x] else find(parent[x])
def union(x,y):
    if x> y:
        parent[x] = y
    else:
        parent[y] = x
def check(x,y):
    if find(x) == find(y):
        return
    temp = 0
    for i,j in ((arr[x][0],arr[x][1]),(arr[x][0],arr[x][3]),(arr[x][2],arr[x][1]),(arr[x][2],arr[x][3])):
        if arr[y][0] < i < arr[y][2] and arr[y][1] < j < arr[y][3]:
            temp += 1
        if (arr[y][0] <= i <= arr[y][2] and j in (arr[y][1],arr[y][3])) or (arr[y][1] <= j <= arr[y][3] and i in (arr[y][0],arr[y][2])):
            union(find(x),find(y))
            return
    if temp%4 != 0:
        union(find(x),find(y))
    
input = sys.stdin.readline
            
N = int(input())
arr = []
parent  = [i for i in range(N)]
ans = 0
for _ in range(N):
    arr.append(list(map(int, input().split())))

for i in range(N):
    for j in range(N):
        check(i,j)


for x in range(N):
    if 0 in (arr[x][1], arr[x][3]) and arr[x][0] <= 0 <= arr[x][3]:
        ans -= 1
        break

grandfa = set()
for x in range(N):
    grandfa.add(find(x))
print(len(grandfa) + ans)
