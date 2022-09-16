from collections import deque
def l(n):
    for i in range(3):
        for j in range(3):
            temp[1+n*(j-1)][1-n*(i-1)] = garo[i][j]
    for i in range(3):
        for j in range(3):
            garo[i][j] = temp[i][j]
    if n == 1:
        for i in range(3):
            sero[0].appendleft(sero[0].pop())
    elif n == -1:
        for i in range(3):
            sero[0].append(sero[0].popleft())

def change(n):
    if n == 0:
        for i in range(3):
            for j in range(12):
                
    elif n == 1:
        return 




garo = [
    deque([1,1,1,2,2,2,3,3,3,5,5,5]),
    deque([1,1,1,2,2,2,3,3,3,5,5,5]),
    deque([1,1,1,2,2,2,3,3,3,5,5,5]),
]
sero = [
    deque([0,0,0,2,2,2,4,4,4,5,5,5]),
    deque([0,0,0,2,2,2,4,4,4,5,5,5]),
    deque([0,0,0,2,2,2,4,4,4,5,5,5]),
]

temp = [[0]*3 for _ in range(3)]

for i in range(5):
    l(1) #1+   , -1:-
    print('#####')
    print(garo[0])
    print(garo[1])
    print(garo[2])
    print()
    print(sero[0])
    print(sero[1])
    print(sero[2])
    print()