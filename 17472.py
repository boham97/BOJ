from cmath import inf
import itertools

x, y = list(map(int,input().split()))

arr = [[0 for i in range (y+2)] for j in range(x+2)]
for i in range(1,x+1):
    arr[i] = list(map(int,input().split()))
    arr[i].append(0)
    arr[i].insert(0,0)

cnt = 1
for i in range(x+2):
    for j in range(y+2):
        if arr[i][j] == 1:
            arr[i][j] = cnt
            cnt += 1
last = [arr[i][:] for i in range(x+2)]
while(1):
    for i in range(x+2):
        for j in range(y+2):
            if arr[i][j] > 0:
                if arr[i][j] < arr[i-1][j]:
                    arr[i-1][j] = arr[i][j]
                if arr[i][j] < arr[i+1][j]:
                    arr[i+1][j] = arr[i][j]
                if arr[i][j] < arr[i][j-1]:
                    arr[i][j-1] = arr[i][j]
                if arr[i][j] < arr[i][j+1]:
                    arr[i][j+1] = arr[i][j]
    if last == arr:
        break
    else:
        last = [arr[i][:] for i in range(x+2)]
island =[]
for i in range(1,x+1):
    for j in range(1,y+1):
        if arr[i][j] != 0 and arr[i][j] not in island:
            island.append(arr[i][j])

mat = [[inf for i in range(len(island))] for j in range(len(island))]

for i in range(1,x+1):
    for j in range(1, y+1):
        if arr[i][j] in island:
            for k in range(j+1,y+2):
                if arr[i][k] != 0:
                    if arr[i][j] == arr[i][k]:
                        break
                    if arr[i][j] != arr[i][k] and mat[island.index(arr[i][j])][island.index(arr[i][k])] > k-j-1:
                        if k-j >2:
                            mat[island.index(arr[i][j])][island.index(arr[i][k])]= k-j-1
                        break
            for k in range(j-1,-1,-1):
                if arr[i][k] != 0:
                    if arr[i][j] == arr[i][k]:
                        break
                    if arr[i][j] != arr[i][k] and mat[island.index(arr[i][j])][island.index(arr[i][k])] > j-k-1:
                        if j-k >2:
                            mat[island.index(arr[i][j])][island.index(arr[i][k])]= j-k-1
                        break
            for k in range(i+1,x+2):
                if arr[k][j] != 0:
                    if arr[i][j] == arr[k][j]:
                        break
                    if arr[i][j] != arr[k][j] and mat[island.index(arr[i][j])][island.index(arr[k][j])] > k-i-1:
                        if k-i >2:
                            mat[island.index(arr[i][j])][island.index(arr[k][j])]= k-i-1
                        break
            for k in range(i-1,-1,-1):
                if arr[k][j] != 0:
                    if arr[i][j] == arr[k][j]:
                        break
                    if arr[i][j] != arr[k][j] and mat[island.index(arr[i][j])][island.index(arr[k][j])] > i-k-1:
                        if i-k >2:
                            mat[island.index(arr[i][j])][island.index(arr[k][j])]= i-k-1
                        break
loute = []
for i in range(len(island)):
    for j in range(i+1,len(island)):
        if mat[i][j] != inf:
            loute.append([i, j, mat[i][j]])

mini = inf
for i in itertools.combinations(range(len(loute)),len(island)-1):
    #print(i)
    set1= set()
    total = 0
    for k in range(len(island)-1):
        for j in i:
            if j == i[0]:
                set1.add(loute[j][0])
                set1.add(loute[j][1])
            elif loute[j][0] in set1 or loute[j][1] in set1:
                set1.add(loute[j][0])
                set1.add(loute[j][1])
            total += loute[j][2]
    total = total // (len(island)-1)
    if total < mini and len(set1) == len(island):
        mini = total
        minloute = i
""" print()
for i in range(x+2):
    for j in range (y+2):
        print(arr[i][j], end=' ')
    print()
print()
print(island)
print()
print(mat) """
if mini == inf:
    print(-1)
else:
    print(mini)
""" print(loute)
print(minloute) """